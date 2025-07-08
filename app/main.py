import streamlit as st
import pandas as pd
from src.data_loader import load_race_data

st.title("🏁 F1 Bayesian Race Predictor")
st.write("Welcome! This app helps simulate race outcomes using Bayesian models.")

if st.button("Load Monaco 2023 Data"):
    df = load_race_data(2023, "Monaco")
    st.dataframe(df)
