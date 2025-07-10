import streamlit as st
import pandas as pd
import sys
import os

# Add the project root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.data_loader import load_race_data

st.title("🏁 F1 Bayesian Race Predictor")
st.write("Welcome! This app helps simulate race outcomes using Bayesian models.")


st.header("📥 Load Race from FastF1")
years = list(range(2018, 2025))
gps = ["Monaco", "Silverstone", "Monza", "Austria", "Spa", "Suzuka", "Abu Dhabi"]

col1, col2 = st.columns(2)
selected_year = col1.selectbox("Year", years)
selected_gp = col2.selectbox("Grand Prix", gps)

DATA_DIR = "data/raw"

def get_race_data(year, gp):
    filename = f"{DATA_DIR}/{gp.lower()}_{year}.csv"
    if os.path.exists(filename):
        df = pd.read_csv(filename)
    else:
        df = load_race_data(year, gp)
    return df


if st.button("Load race data"):
    with st.spinner("Loading race data..."):
        df = get_race_data(selected_year, selected_gp)

        # Convert timedelta columns to string for display
        time_cols = ['LapTime', 'PitOutTime', 'PitInTime']
        for col in time_cols:
            if col in df.columns:
                df[col] = df[col].apply(lambda x: str(x) if pd.notna(x) else '')

        st.dataframe(df)
        st.success(f"Data loaded and cached: {selected_gp} {selected_year}")