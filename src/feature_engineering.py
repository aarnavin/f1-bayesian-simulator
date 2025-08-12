import pandas as pd
import numpy as np
import datetime as dt

def engineer_features(df):
    laps = df.copy()
    
    # Convert times to seconds
    for col in ["LapTime", "Sector1Time", "Sector2Time", "Sector3Time"]:
        laps[col] = pd.to_timedelta(df[col], errors='coerce')
        laps[f"{col} (s)"] = laps[col].dt.total_seconds()

    # Aggregate driver statistics
    agg_df = laps.groupby("Driver")[["LapTime (s)", "Sector1Time (s)", "Sector2Time (s)", "Sector3Time (s)"]].mean().reset_index()
    # 2025 Qualifying Data Chinese GP
    qualifying_2025 = pd.DataFrame({
        "Driver": ["Oscar Piastri", "George Russell", "Lando Norris", "Max Verstappen", "Lewis Hamilton",
                "Charles Leclerc", "Isack Hadjar", "Andrea Kimi Antonelli", "Yuki Tsunoda", "Alexander Albon",
                "Esteban Ocon", "Nico Hülkenberg", "Fernando Alonso", "Lance Stroll", "Carlos Sainz Jr.",
                "Pierre Gasly", "Oliver Bearman", "Jack Doohan", "Gabriel Bortoleto", "Liam Lawson"],
        "QualifyingTime (s)": [90.641, 90.723, 90.793, 90.817, 90.927,
                            91.021, 91.079, 91.103, 91.638, 91.706,
                            91.625, 91.632, 91.688, 91.773, 91.840,
                            91.992, 92.018, 92.092, 92.141, 92.174]
    })

    # Map full names to FastF1 3-letter codes
    driver_mapping = {
        "Oscar Piastri": "PIA", "George Russell": "RUS", "Lando Norris": "NOR", "Max Verstappen": "VER",
        "Lewis Hamilton": "HAM", "Charles Leclerc": "LEC", "Isack Hadjar": "HAD", "Andrea Kimi Antonelli": "ANT",
        "Yuki Tsunoda": "TSU", "Alexander Albon": "ALB", "Esteban Ocon": "OCO", "Nico Hülkenberg": "HUL",
        "Fernando Alonso": "ALO", "Lance Stroll": "STR", "Carlos Sainz Jr.": "SAI", "Pierre Gasly": "GAS",
        "Oliver Bearman": "BEA", "Jack Doohan": "DOO", "Gabriel Bortoleto": "BOR", "Liam Lawson": "LAW"
    }

    qualifying_2025["DriverCode"] = qualifying_2025["Driver"].map(driver_mapping)

    # Merge qualifying data with sector times
    agg_df = agg_df.rename(columns={"Driver": "DriverCode"})
    merged_data = qualifying_2025.merge(agg_df, on="DriverCode", how="left")
    return merged_data
