import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import warnings
warnings.filterwarnings('ignore')

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_data(filepath):
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} emails")
    print(f"Class distribution:\n{df['label'].value_counts()}\n")
    return df


def train_models(df):
    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], 
        df['label'], 
        test_size=0.2, 
        random_state=42
    )
    
    print(f"Training set size: {len(X_train)}")
    print(f"Test set size: {len(X_test)}\n")
    
    print("Creating TF-IDF vectorizer...")
    tfidf = TfidfVectorizer(
        max_features=5000,
        min_df=1,
        max_df=0.8,
        lowercase=True,
        stop_words='english',
        ngram_range=(1, 2)
    )
    
    X_train_tfidf = tfidf.fit_transform(X_train)
    X_test_tfidf = tfidf.transform(X_test)
    
    print(f"TF-IDF shape: {X_train_tfidf.shape}\n")
    
    print("Training Naive Bayes model...")
    nb_model = MultinomialNB()
    nb_model.fit(X_train_tfidf, y_train)
    nb_pred = nb_model.predict(X_test_tfidf)
    
    print(f"Naive Bayes Accuracy: {accuracy_score(y_test, nb_pred):.4f}")
    print(f"Naive Bayes Precision: {precision_score(y_test, nb_pred, pos_label='phishing'):.4f}")
    print(f"Naive Bayes Recall: {recall_score(y_test, nb_pred, pos_label='phishing'):.4f}")
    print(f"Naive Bayes F1-Score: {f1_score(y_test, nb_pred, pos_label='phishing'):.4f}\n")
    
    print("Training Logistic Regression model...")
    lr_model = LogisticRegression(max_iter=1000, random_state=42)
    lr_model.fit(X_train_tfidf, y_train)
    lr_pred = lr_model.predict(X_test_tfidf)
    
    print(f"Logistic Regression Accuracy: {accuracy_score(y_test, lr_pred):.4f}")
    print(f"Logistic Regression Precision: {precision_score(y_test, lr_pred, pos_label='phishing'):.4f}")
    print(f"Logistic Regression Recall: {recall_score(y_test, lr_pred, pos_label='phishing'):.4f}")
    print(f"Logistic Regression F1-Score: {f1_score(y_test, lr_pred, pos_label='phishing'):.4f}\n")
    
    return tfidf, nb_model, lr_model


def save_models(tfidf, nb_model, lr_model, model_dir='models'):
    os.makedirs(model_dir, exist_ok=True)
    
    with open(os.path.join(model_dir, 'tfidf_vectorizer.pkl'), 'wb') as f:
        pickle.dump(tfidf, f)
    
    with open(os.path.join(model_dir, 'naive_bayes_model.pkl'), 'wb') as f:
        pickle.dump(nb_model, f)
    
    with open(os.path.join(model_dir, 'logistic_regression_model.pkl'), 'wb') as f:
        pickle.dump(lr_model, f)
    
    print(f"Models saved to '{model_dir}/' directory")


if __name__ == "__main__":
    data_path = os.path.join(SCRIPT_DIR, 'data', 'sample_emails.csv')
    df = load_data(data_path)
    
    tfidf, nb_model, lr_model = train_models(df)
    
    model_dir = os.path.join(SCRIPT_DIR, 'models')
    save_models(tfidf, nb_model, lr_model, model_dir)
    
    print("\nTraining complete! Models saved successfully.")
