# generate_report.py

import pandas as pd
import logging

from pathlib import Path
from datetime import datetime

# ======================
# Paths
# ======================

BASE_DIR = Path(__file__).resolve().parent.parent


LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "pipeline.log"

REPORTS_DIR = BASE_DIR / "reports"

METRICS_PATH = REPORTS_DIR / "model_metrics.csv"

REPORT_PATH = REPORTS_DIR / "model_summary.md"


# Crear carpetas necesarias

LOG_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# =======================
# Logging
# =======================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Starting report generation pipeline")


try:

    if not METRICS_PATH.exists():
        raise FileNotFoundError(
            f"Metrics file not found: {METRICS_PATH}"
        )


    metrics_df = pd.read_csv(METRICS_PATH)
    
    if metrics_df.empty:
        raise ValueError(
            "metrics dataframe is empty"
        )

    logging.info(
        f"Metrics loaded successfully with {len(metrics_df)} records"
)


    logging.info(
        "Calculating best model based on R2 score"
)

    best_model = metrics_df.loc[
        metrics_df["R2"].idxmax(),
        "Model"
]

    
    logging.info(
        f"Best model identified: {best_model}"
)

# Crear reporte markdown

    report_content = f"""
    # Model Training Report

    ## Execution Date

    {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


    ## Model Metrics

    {metrics_df.to_markdown(index=False)}


    ## Best Model

    {best_model}

"""

# Guardar reporte

    with open(REPORT_PATH, "w", encoding="utf-8") as file:
        file.write(report_content)
    
    logging.info(
        f"Report generated successfully at {REPORT_PATH}"
)
    
    logging.info(
        "Report generation pipeline finished successfully"
    )


except Exception:
    
    logging.exception(
        "Report generation pipeline failed"
    )
    
    
    raise