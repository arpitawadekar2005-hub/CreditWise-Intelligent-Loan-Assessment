
# 🏦 CreditWise – Intelligent Loan Assessment System

![Banner Image](Images/banner.png)

# Problem Statement

A mid-sized financial company named SecureTrust Bank offers personal and home loans to customers across urban and rural regions of India. Every day, hundreds of customers apply for loans through online and branch applications.

Until now, SecureTrust Bank has been using a manual verification process where loan officers evaluate applications by checking income proofs, employment details, credit history, and other documents. This process is time-consuming, biased, and inconsistent.

As a result, the bank faces two major challenges:

1. Good customers sometimes get rejected, leading to loss of business.
2. High-risk customers sometimes get approved, leading to financial losses.

To solve this problem, the bank wants to introduce an intelligent loan approval system powered by Machine Learning that can automatically analyse applicant details and predict whether a loan should be Approved or Rejected before final human verification.

---

# Goal of this Project

The objective of this project is to automate the loan approval process based on customer details provided during the loan application process.

The system analyses applicant financial, personal, and credit-related information and predicts whether a loan application should be approved or rejected.

The goal is to:

* Reduce manual effort
* Improve consistency in decision making
* Minimize financial risk
* Speed up loan approval
* Provide unbiased predictions

---

# Hypothesis Generation

Below are the factors that may influence loan approval decisions:

* Applicant with higher income may have higher chances of loan approval.
* Applicants with higher credit scores are more likely to receive loan approval.
* Higher savings balance may improve approval chances.
* Applicants with fewer existing loans may have lower default risk.
* Lower Debt-to-Income Ratio (DTI) may increase approval probability.
* Higher collateral value may positively impact approval decisions.
* Smaller loan amounts may have higher approval chances.
* Stable employment may increase approval probability.

---

# Data Source

The dataset consists of historical loan application records collected by SecureTrust Bank.

Each record represents a loan applicant and contains personal, financial, employment, and credit-related information.

The target variable is:

**Loan_Approved**

* 1 = Approved
* 0 = Rejected

---

# Data Dictionary

| Variable           | Description                             |
| ------------------ | --------------------------------------- |
| Applicant_ID       | Unique applicant ID                     |
| Applicant_Income   | Monthly income of applicant             |
| Coapplicant_Income | Monthly income of co-applicant          |
| Employment_Status  | Salaried / Self-Employed / Business     |
| Age                | Applicant age                           |
| Marital_Status     | Married / Single                        |
| Dependents         | Number of dependents                    |
| Credit_Score       | Credit bureau score                     |
| Existing_Loans     | Number of already running loans         |
| DTI_Ratio          | Debt-to-Income ratio                    |
| Savings            | Savings balance                         |
| Collateral_Value   | Value of collateral provided            |
| Loan_Amount        | Loan amount requested                   |
| Loan_Term          | Loan duration (months)                  |
| Loan_Purpose       | Home / Education / Personal / Business  |
| Property_Area      | Urban / Semi-Urban / Rural              |
| Education_Level    | Graduate / Postgraduate / Undergraduate |
| Gender             | Male / Female                           |
| Employer_Category  | Govt / Private / Self                   |
| Loan_Approved      | Target Variable                         |

---

# Data Cleaning

* Checked missing values
* Removed inconsistencies
* Verified data types
* Prepared data for machine learning models

---

## Exploratory Data Analysis (EDA)

### 1. Loan Approval Distribution

This plot shows the distribution of approved and rejected loan applications.

![Loan Approval Distribution](Images/loan_approval_distribution.png)

---

### 2. Education Level Distribution

This visualization shows the number of Graduate and Non-Graduate applicants in the dataset.

![Education Level Distribution](Images/education_level_distribution.png)

---

### 3. Correlation Heatmap

The heatmap illustrates the correlation between numerical features used for loan approval prediction.

![Correlation Heatmap](Images/correlation_heatmap.png)

---

### 4. Feature Analysis

Boxplots comparing Applicant Income, Credit Score, Debt-to-Income Ratio (DTI), and Savings against loan approval status.

![Feature Analysis](Images/feature_analysis.png)

---

### 5. Credit Score vs Loan Approval

This histogram highlights the relationship between applicant credit scores and loan approval outcomes.

![Credit Score vs Loan Approval](Images/credit_score_vs_approval.png)

# Feature Engineering

Additional features created:

* DTI_Ratio_sq
* Credit_Score_sq

These features help capture non-linear relationships within the data.

---

# Feature Transformation

### Label Encoding

Applied on:

* Education_Level
* Loan_Approved

### One Hot Encoding

Applied on:

* Employment_Status
* Marital_Status
* Loan_Purpose
* Property_Area
* Gender
* Employer_Category

### Feature Scaling

Used StandardScaler for normalization of numerical features.

---

# Model Building

The following machine learning models were trained and evaluated:

### Logistic Regression

### K-Nearest Neighbors (KNN)

### Gaussian Naive Bayes

---

# Model Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

(Add screenshots of results here)

---

# Final Model

### Gaussian Naive Bayes

The Gaussian Naive Bayes model was selected as the final model based on its performance on the processed dataset.

---

# Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Encoding
   ↓
Feature Engineering
   ↓
Scaling
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

# Future Improvements

* Explainable AI
* Real-time prediction dashboard
* Web deployment
* Ensemble learning models

---

# Author

**Arpita Wadekar**

Electronics & Communication Engineering
Jain College of Engineering, Belagavi
