import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import os

# CREATE IMAGES FOLDER
os.makedirs("images", exist_ok=True)

# LOAD DATA
X = pd.read_csv("data/processed_features.csv")
y = pd.read_csv("data/target.csv").values.ravel()

print("Data Loaded Successfully")

# SAME FEATURE ENGINEERING
X['performance_score'] = (X['attendance'] + X['marks']) / 2

# TRAIN-TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# LOAD MODEL
model = joblib.load("app/model.pkl")

print("Model Loaded Successfully")

# PREDICTION
y_pred = model.predict(X_test)

# EVALUATION
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.4f}")
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
