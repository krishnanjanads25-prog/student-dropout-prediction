# 🎓 Student Dropout Prediction using Machine Learning

## 📌 Project Overview

This project aims to predict whether a student is at risk of dropping out using machine learning techniques. By analyzing academic, behavioral, and socio-economic factors, we build predictive models to identify at-risk students early and support timely intervention.

---

## 🎯 Problem Statement

Student dropout is a major concern in educational institutions. Early prediction of dropout risk can help institutions take preventive measures.
This project focuses on building a predictive model that classifies students into:

* **High Dropout Risk**
* **Low Dropout Risk**

---

## 📊 Dataset Description

The dataset contains various features related to student performance and background:

### 🔹 Features include:

* Age
* Gender
* Family Income
* Internet Access
* Study Hours per Day
* Attendance Rate
* Assignment Delay Days
* Travel Time
* Part-time Job
* Scholarship
* Stress Index
* GPA / CGPA
* Semester
* Department
* Parental Education

### 🎯 Target Variable:

* `dropout` (0 = No, 1 = Yes)

---

## 🔄 Project Workflow

### 1️⃣ Data Preprocessing

* Handling missing values
* Removing duplicates
* Encoding categorical variables
* Feature scaling
* Outlier handling

---

### 2️⃣ Exploratory Data Analysis (EDA)

* Dropout distribution analysis
* Correlation heatmaps
* Feature vs dropout visualizations
* Key insights:

  * Low GPA → Higher dropout risk
  * Low attendance → Strong indicator
  * High stress → Increased risk

---

### 3️⃣ Feature Engineering

* Created derived features (e.g., performance score)
* Selected important features for modeling

---

### 4️⃣ Model Building

We trained and compared multiple models:

* Logistic Regression
* Random Forest
* XGBoost

---

### 5️⃣ Model Evaluation

Metrics used:


* F1 Score
* ROC-AUC

📌 Random Forest is the best model for this problem because it achieved the highest F1 Score, which is more important for imbalanced classification.

📌 Logistic Regression showed the highest ROC-AUC, indicating strong class separation ability.

📌 Therefore, Random Forest is selected as the final model.

---

## 📈 Results Summary

| Model               | F1 Score | ROC-AUC |
|--------------------|----------|---------|
| Logistic Regression| 0.50     | 0.82    |
| Random Forest      | 0.55     | 0.79    |
| XGBoost            | 0.54     | 0.77    |

📌 Random Forest achieved the highest F1 Score, making it the best model for classification performance.

📌 Logistic Regression achieved the highest ROC-AUC, indicating strong ability to distinguish between dropout and non-dropout cases.


### 6️⃣ Model Explainability

* Used SHAP (optional enhancement)
* Identified key influencing features:

  * GPA
  * Attendance
  * Stress Index

---

### 7️⃣ Deployment

The model is deployed using **Streamlit**.

### 🌐 Live App:

👉 *(https://student-dropout-prediction-g9vasalu3gaa2plehhy5gw.streamlit.app/)*

---

## 🖥️ How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/Akshay44151/student-dropout-prediction.git
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Application

```bash
streamlit run 03_app.py
```

---

## 📁 Project Structure

```text
student-dropout-prediction/
│
├── data/
│   └── student_dropout_dataset_v3.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Modeling.ipynb
│   └── member1_preprocessing.py
│
├── best_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── presentation.pptx
```

---

## 👥 Team Members

* Member 1 → Data Preprocessing
* Member 2 → Model Development
* Member 3 → Deployment

📌 All members contributed across all stages of the project lifecycle.

---

## ⚠️ Limitations

* Limited dataset size
* Possible bias in features
* Model performance depends on data quality

---

## 🚀 Future Work

* Use deep learning models
* Add real-time student monitoring
* Integrate with institutional systems
* Improve feature engineering

---

## 📌 Conclusion

This project demonstrates how machine learning can effectively predict student dropout risk. Early identification of at-risk students can significantly improve retention rates and academic outcomes.

---

## 🔗 Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* XGBoost
* Seaborn, Matplotlib
* Streamlit
* GitHub

---

## ⭐ Acknowledgment

This project was developed as part of the Predictive Analytics course, focusing on real-world machine learning application and collaboration.
