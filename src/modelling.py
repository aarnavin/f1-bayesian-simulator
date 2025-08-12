from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
from src.feature_engineering import engineer_features
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd

def train_regression_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = GradientBoostingRegressor(n_estimators=200, learning_rate=0.1, random_state=42)
    model.fit(X_train, y_train)
    return model

def predict_podium(df):
    features_df = engineer_features(df)

    X = features_df[["QualifyingTime (s)", "Sector1Time (s)", "Sector2Time (s)", "Sector3Time (s)"]].fillna(0)
    y = features_df.groupby("Driver")["LapTime (s)"].mean().reset_index()["LapTime (s)"]

    model = train_regression_model(X, y)
    y_pred = model.predict(X)

    features_df["PredictedPosition (s)"] = y_pred
    podium_df = features_df.sort_values("PredictedPosition").head(3)
    return podium_df