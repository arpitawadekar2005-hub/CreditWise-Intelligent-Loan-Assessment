import streamlit as st
import pickle
import numpy as np

# Load model
import os

st.write("Files in directory:", os.listdir())

model = pickle.load(open("model.pkl", "rb"))

st.title("🏦 CreditWise Loan Approval System")

st.write("Enter applicant details")

income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)
age = st.number_input("Age", min_value=18)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (Months)", min_value=1)

if st.button("Predict"):

    input_data = np.array([
        income,
        co_income,
        age,
        credit_score,
        loan_amount,
        loan_term
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
