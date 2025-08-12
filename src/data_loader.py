import fastf1
import pandas as pd
import os
    
DATA_DIR = "data/raw"

def load_race_data(year, gp, session_type="R"):
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    # results = session.results
    # results = results[['Abbreviation', 'Position']]
    laps = session.laps
    laps = laps[["Driver", "LapTime", "Sector1Time", "Sector2Time", "Sector3Time"]].copy()
    laps.dropna(inplace=True)
    # merged = laps.merge(results, left_on='Driver', right_on='Abbreviation')

    os.makedirs("data/raw", exist_ok=True)    

    filename = f"{DATA_DIR}/{gp.lower()}_{year}.csv"
    laps.to_csv(filename, index=False)
    print(f"✅ Saved {gp} {year} race data.")
    return laps

