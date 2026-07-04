# 1.Imports

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODELS_DIR = BASE_DIR / "models"
REPORTS_DIR = BASE_DIR / "reports"
DATA_PATH = BASE_DIR / "datasets" / "processed" / "car_manufacturing_clean.csv"

MODELS_DIR.mkdir(exist_ok=True)
REPORTS_DIR.mkdir(exist_ok=True)




# 2.Load data

df = pd.read_csv(DATA_PATH)


# 3.Features/target
df = pd.get_dummies(df, columns=['Engine_Type', 'Production_Line'], drop_first=True)
drop_cols = ['Cost','Car_ID','Production_Date']
X = df.drop(columns=drop_cols)
y = df['Cost']


# 4.Split
X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)


# 5.Linear model
model_linear = LinearRegression()
model_linear.fit(X_train, y_train)

y_pred_linear = model_linear.predict(X_test)

mse_linear = mean_squared_error(y_test, y_pred_linear)
r2_linear = r2_score(y_test, y_pred_linear)

joblib.dump(
    model_linear, 
    MODELS_DIR / "baseline_linear_regression.joblib"
)


# 6.Random Forest
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)


mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf =  r2_score(y_test, y_pred_rf)


joblib.dump(
    rf_model,
    MODELS_DIR / "random_forest_baseline.joblib"
)


# 7. Metrics report

metrics_df = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest"],
    "MSE": [mse_linear, mse_rf],   
    "R2": [r2_linear, r2_rf]       
})


metrics_df.to_csv(
    REPORTS_DIR / "model_metrics.csv",
    index=False
)









