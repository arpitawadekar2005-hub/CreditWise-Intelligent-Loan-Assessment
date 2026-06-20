# 🏦 CreditWise – Intelligent Loan Assessment System

## 📌 Project Overview

CreditWise is a Machine Learning based loan approval prediction system developed to assist financial institutions in evaluating loan applications efficiently.

The system analyzes an applicant's financial profile, credit history, employment details, and demographic information to predict whether a loan should be approved or rejected.

---

## 🎯 Problem Statement

Traditional loan approval processes often involve manual assessment of multiple applicant factors, making the process time-consuming and prone to inconsistencies.

This project automates the loan assessment process using Machine Learning techniques to support faster and more consistent decision-making.

---

## 📊 Dataset Features

The model uses the following applicant information:

- Applicant Income
- Coapplicant Income
- Age
- Dependents
- Existing Loans
- Savings
- Collateral Value
- Loan Amount
- Loan Term
- Education Level
- Employment Status
- Marital Status
- Loan Purpose
- Property Area
- Gender
- Employer Category
- Credit Score
- Debt-to-Income Ratio (DTI)

---

## ⚙️ Data Preprocessing

The following preprocessing techniques were applied:

### Label Encoding
Applied on:
- Education_Level
- Loan_Approved

### One-Hot Encoding
Applied on:
- Employment_Status
- Marital_Status
- Loan_Purpose
- Property_Area
- Gender
- Employer_Category

### Feature Scaling
- StandardScaler

### Feature Engineering

Additional features created:

- DTI_Ratio_sq
- Credit_Score_sq

These engineered features improved model learning by capturing non-linear relationships.

---

## 🤖 Machine Learning Models Evaluated

Multiple algorithms were trained and compared:

### 1. Logistic Regression
Used as a baseline classification model.

### 2. K-Nearest Neighbors (KNN)
Distance-based classification approach.

### 3. Gaussian Naive Bayes
Probabilistic classification algorithm.

---

## 📈 Model Evaluation Metrics

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 🏆 Final Model

### Gaussian Naive Bayes

The Gaussian Naive Bayes classifier was selected as the final model due to its strong performance and efficient handling of numerical features after preprocessing and feature engineering.

---

## 🔄 Project Workflow

```text
Data Collection
       ↓
Data Cleaning
       ↓
Label Encoding
       ↓
One-Hot Encoding
       ↓
Feature Engineering
       ↓
Feature Scaling
       ↓
Train-Test Split
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Loan Approval Prediction
```

---

## 📂 Repository Structure

```text
CreditWise-Intelligent-Loan-Assessment
│
├── README.md
├── credit_wise.ipynb
├── model.pkl
├── requirements.txt
├── dataset/
└── screenshots/
```

---

## 📸 Project Screenshots

### Dataset Preview

![Dataset](screenshots/dataset_preview.png)

### Data Preprocessing

![Preprocessing](screenshots/preprocessing.png)

### Model Comparison

![Comparison](screenshots/model_comparison.png)

### Confusion Matrix

![Confusion Matrix](screenshots/confusion_matrix.png)

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Jupyter Notebook
- Matplotlib
- Seaborn

---

## 🚀 Future Enhancements

- Web-based deployment
- Real-time loan approval dashboard
- Explainable AI for decision transparency
- Ensemble learning approaches

---

## 👩‍💻 Author

**Arpita Wadekar**

Electronics and Communication Engineering  
Jain College of Engineering, Belagavi

### Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Model Evaluation
- Classification Algorithms
- Python Programming
