# data_cleaning.py

import pandas as pd
import logging
from pathlib import Path

# =======================
# Paths
# =======================

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"

LOG_FILE = LOG_DIR / "pipeline.log"

DATA_PATH = BASE_DIR / "datasets" / "raw" / "car_manufacturing_data.csv"

OUTPUT_PATH = BASE_DIR / "datasets" / "processed" / "car_manufacturing_clean.csv"


# Crear carpetas necesarias

LOG_DIR.mkdir(exist_ok=True)


# =======================
# Logging
# =======================


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Starting data cleaning pipeline")

# Ruta del conjunto de datos de entrada

try:

    logging.info("Loading raw dataset")

    df = pd.read_csv(DATA_PATH)
    
    logging.info(
        f"Dataset loaded successfully with {len(df)} rows"
    )


# Guardar copia del dataset original
    logging.info("Creating backup of original dataset")

    df_original = df.copy()

# Eliminar duplicados, conservando el primer  registro según el índice

    rows_before = len(df)

    df = df.drop_duplicates(
    subset=['Car_ID', 'Production_Date'], 
    keep='first'
)

    rows_after = len(df)

    logging.info(
    f"Removed {rows_before - rows_after} duplicated records"
)


# Eliminar filas con Cost nulo

    rows_before = len(df)

    df = df.dropna(subset=['Cost'])

    rows_after = len(df)

    logging.info(
    f"Removed {rows_before - rows_after} rows with missing Cost values"
)


# Guardar conjunto de datos procesado

    logging.info(
        f"Cleaned dataset contains {len(df)} rows"
    )

    logging.info(
    f"Saving cleaned dataset to {OUTPUT_PATH}"
)

    df.to_csv(OUTPUT_PATH, index=False)


# Validación rápida

    expected_rows = 90
    actual_rows = df.shape[0]


    if actual_rows != expected_rows:
    
        logging.warning(
            f"Expected {expected_rows} rows but found {actual_rows}"
    )

    else:
    
        logging.info(
            f"Dataset cleaned successfully ({actual_rows} rows)"
    )

    logging.info("Data cleaning pipeline finished successfully")

except Exception:
    
    logging.exception("Data cleaning pipeline failed")
    
    raise