import fastf1
import pandas as pd
import os
    
DATA_DIR = "data/raw"

def load_race_data(year, gp, session_type="R"):
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    laps = session.laps
    driver_laps = laps[["Driver", "LapTime", "Team", "Compound", "LapNumber", "PitOutTime", "PitInTime"]]

    os.makedirs("data/raw", exist_ok=True)    

    filename = f"{DATA_DIR}/{gp.lower()}_{year}.csv"
    driver_laps.to_csv(filename, index=False)
    print(f"Saved {gp} {year} race data.")
    return driver_laps
