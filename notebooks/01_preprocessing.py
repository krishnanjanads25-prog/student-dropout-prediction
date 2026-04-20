import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
import os

# ===============================
# 0. CREATE REQUIRED FOLDERS
# ===============================
os.makedirs("data", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("app", exist_ok=True)

# ===============================
# 1. LOAD DATA
# ===============================
df = pd.read_csv("student_dropout_dataset_v3.csv")

# ===============================
# 2. CLEAN COLUMN NAMES
# ===============================
df.columns = df.columns.str.strip().str.lower()

df.rename(columns={
    'attendance_rate': 'attendance',
    'gpa': 'marks'
}, inplace=True)

print("Initial Data Shape:", df.shape)

# ===============================
# 3. HANDLE MISSING VALUES
# ===============================
print("\nMissing values before:\n", df.isnull().sum())

# Fill numeric with median
df.fillna(df.median(numeric_only=True), inplace=True)

# Fill categorical with "Unknown"
df.fillna("Unknown", inplace=True)

print("\nMissing values after:\n", df.isnull().sum())

# ===============================
# 4. EDA (SAVE PNG FILES)
# ===============================

# Dropout distribution
plt.figure()
sns.countplot(x='dropout', data=df)
plt.title("Dropout Distribution")
plt.savefig("images/dropout_distribution.png")
plt.close()

# Marks vs Dropout
plt.figure()
sns.boxplot(x='dropout', y='marks', data=df)
plt.title("Marks vs Dropout")
plt.savefig("images/marks_vs_dropout.png")
plt.close()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("images/correlation_heatmap.png")
plt.close()

# ===============================
# 5. ENCODE CATEGORICAL FEATURES
# ===============================
label_encoders = {}

for col in df.select_dtypes(include=['object', 'string']):
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# ===============================
# 6. FEATURE & TARGET SPLIT
# ===============================
X = df.drop('dropout', axis=1)
y = df['dropout']

# ===============================
# 7. FEATURE SCALING
# ===============================
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# ===============================
# 8. SAVE OUTPUT FILES
# ===============================
X_scaled.to_csv("data/processed_features.csv", index=False)
y.to_csv("data/target.csv", index=False)

# Save scaler & encoders (for app)
joblib.dump(scaler, "app/scaler.pkl")
joblib.dump(label_encoders, "app/encoders.pkl")

# ===============================
# 9. FINAL MESSAGE
# ===============================
print("\n✅ Preprocessing completed successfully!")
print("Files created:")
print("- data/processed_features.csv")
print("- data/target.csv")
print("- images/*.png")
print("- app/scaler.pkl")
print("- app/encoders.pkl")

# ======================================
# Member 2
# ======================================

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Handle outliers using IQR
for col in df.select_dtypes(include=['int64', 'float64']).columns:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = df[col].clip(lower, upper)

# Feature scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[num_cols] = scaler.fit_transform(df[num_cols])

print("✅ Additional preprocessing done by Member 2")
