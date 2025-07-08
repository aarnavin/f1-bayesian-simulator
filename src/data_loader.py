import fastf1
import pandas as pd
import os

def load_race_data(year, gp, session_type="R"):
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    laps = session.laps
    driver_laps = laps[["Driver", "LapTime", "Team", "Compound", "LapNumber", "PitOutTime", "PitInTime"]]
    return driver_laps

if __name__ == "__main__":
    df = load_race_data(2023, "Monaco")
    os.makedirs("data/raw", exist_ok=True)
    df.to_csv("data/raw/monaco_2023.csv", index=False)
    print("Saved Monaco 2023 race data.")
