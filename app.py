import streamlit as st
import pandas as pd

st.title("Employee Attrition Analysis Dashboard")

st.write("Employee Attrition Analysis using Business Analytics")

df = pd.read_csv("Palo Alto Networks.csv.xls")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Summary Statistics")
st.write(df.describe())

st.success("Project deployed successfully using Streamlit")
