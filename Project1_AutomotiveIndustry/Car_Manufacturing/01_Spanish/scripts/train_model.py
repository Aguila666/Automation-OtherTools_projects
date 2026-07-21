# 1.Imports

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_squared_error, r2_score
import logging
from pathlib import Path

# =====================
# Paths
# =====================

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "pipeline.log"

MODELS_DIR = BASE_DIR / "models"

REPORTS_DIR = BASE_DIR / "reports"

DATA_PATH = BASE_DIR / "datasets" / "processed" / "car_manufacturing_clean.csv"

# Crear carpetas necesarias

MODELS_DIR.mkdir(parents=True, exist_ok=True)

REPORTS_DIR.mkdir(parents=True, exist_ok=True)

LOG_DIR.mkdir(parents=True, exist_ok=True)


# ===================
# Logging
# ===================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Starting train model pipeline")


# 2.Load data

try:
    
    logging.info("Loading cleaned dataset")

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}"
        ) 
    
    df = pd.read_csv(DATA_PATH)
    
    
    
    logging.info(
        f"Dataset loaded successfully with {len(df)} rows"
    )

    if df.empty:
        raise ValueError("Dataset is empty.")

# 3.Features/target

    logging.info("Encoding categorical variables")
    
    df = pd.get_dummies(df, columns=['Engine_Type', 'Production_Line'], drop_first=True)
    drop_cols = ['Cost','Car_ID','Production_Date']
    X = df.drop(columns=drop_cols)
    y = df['Cost']

    logging.info(
        f"Dataset ready with {X.shape[0]} rows and {X.shape[1]} features"
    )

# 4.Split

    logging.info(
        "Splitting dataset into training and testing sets"
)
    
    X_train, X_test, y_train, y_test = train_test_split(
    X,y, test_size=0.2, random_state=42
)

    logging.info(
        f"Training samples: {len(X_train)} | Testing samples: {len(X_test)}"
    )

# 5.Linear model

    logging.info(
        "Training Linear Regression model"
    )

    model_linear = LinearRegression()
    model_linear.fit(X_train, y_train)

    y_pred_linear = model_linear.predict(X_test)

    mse_linear = mean_squared_error(y_test, y_pred_linear)
    r2_linear = r2_score(y_test, y_pred_linear)
    
    logging.info(
        "Linear Regression evaluation completed"
    )

    logging.info(
        "Saving Linear Regression model"
    )

    joblib.dump(
        model_linear, 
        MODELS_DIR / "baseline_linear_regression.joblib"
    )
    
    logging.info(
        "Linear Regression model saved successfully"
    )   

    logging.info(
        "Linear Regression training completed"
    )

# 6.Random Forest

    logging.info(
        "Training Random Forest model"
    )

    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train, y_train)

    y_pred_rf = rf_model.predict(X_test)


    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf =  r2_score(y_test, y_pred_rf)
    
    logging.info(
        "Random Forest evaluation completed"
    )


    logging.info(
        "Saving Random Forest model"
    )

    joblib.dump(
        rf_model,
        MODELS_DIR / "random_forest_baseline.joblib"
    )
    
    logging.info(
        "Random Forest model saved successfully"
    )

    logging.info(
        "Random Forest training completed"
    )

# 7. Metrics report

    metrics_df = pd.DataFrame({
        "Model": ["Linear Regression", "Random Forest"],
        "MSE": [mse_linear, mse_rf],   
        "R2": [r2_linear, r2_rf]       
})

    logging.info(
        f"Linear Regression -> MSE={mse_linear:.2f}, R2={r2_linear:.4f}"
    )
    
    logging.info(
        f"Random Forest -> MSE={mse_rf:.2f}, R2={r2_rf:.4f}"
    )

    logging.info(
        "Saving model metrics report"
    )

    metrics_df.to_csv(
        REPORTS_DIR / "model_metrics.csv",
        index=False
)
    
    logging.info(
        "Metrics report saved successfully"
    )

    logging.info("Model training pipeline finished successfully")

except Exception:
    
    logging.exception("Model training pipeline failed")
    
    raise