import streamlit as st
import pandas as pd

st.title("💰 Expense Tracker Dashboard")

df = pd.read_csv("data/cleaned_expenses.csv")

categories = st.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

filtered = df[df["Category"].isin(categories)]

st.subheader("📊 Category Wise Spending")
st.bar_chart(filtered.groupby("Category")["Amount"].sum())

st.subheader("📈 Monthly Trend")
st.line_chart(filtered.groupby("Month")["Amount"].sum())

st.subheader("📄 Data Preview")
st.dataframe(filtered)