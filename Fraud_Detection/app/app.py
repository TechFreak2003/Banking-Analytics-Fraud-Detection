import streamlit as st
from datetime import datetime
from src.predict import predict_fraud

st.title("💳 Banking Fraud Detection System")

amount = st.number_input("Transaction Amount")
transaction_type = st.selectbox("Transaction Type", ["Debit", "Credit"])
method = st.selectbox("Transaction Method", ["Online", "ATM", "Branch"])
bank = st.selectbox("Bank Name", ["SBI", "HDFC", "ICICI"])
date = st.datetime_input("Transaction Date", datetime.now())

if st.button("Check Fraud"):
    input_data = {
        "Amount": amount,
        "Transaction Type": transaction_type,
        "Transaction Method": method,
        "Bank Name": bank,
        "Transaction Date": date
    }

    result = predict_fraud(input_data)
    st.success(f"Prediction: {result}")