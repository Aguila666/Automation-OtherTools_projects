# car_manufacturing_pipeline.py

# ================================
# Imports
# ================================

from airflow import DAG

from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

import subprocess

from pathlib import Path


# ================================
# Default arguments
# ================================

default_args = {
    "owner":"JC",
    
    "depends_on_past":False,
    
    "email_on_failure":False,
    
    "email_on_retry":False,
    
    "retries":1,
    
    "retry_delay":timedelta(minutes=5)
    
}



# ================================
# Paths
# ================================

BASE_DIR = Path(__file__).resolve().parent.parent


SCRIPTS_DIR = (
    BASE_DIR / "scripts"
)



DATA_CLEANING_SCRIPT = (
    SCRIPTS_DIR / "data_cleaning.py"
)



TRAIN_MODEL_SCRIPT = (
    SCRIPTS_DIR / "train_model.py"
)

GENERATE_REPORT_SCRIPT = (
    SCRIPTS_DIR / "generate_report.py"
)


# ================================
# Helper Functions
# ================================

def execute_python_script(script_path):
    
    subprocess.run(
        
        ["python", str(script_path)],
        
        check=True
        
    )



# ================================
# Tasks Functions
# ================================

def run_data_cleaning():
    
    try:
    
        print(
        
            f"Executing: {DATA_CLEANING_SCRIPT}"
        
        )
    
    
        execute_python_script(
        
            DATA_CLEANING_SCRIPT
        
        )
        
        print(
            "Task completed successfully"
        )
    

    except Exception:
    
    
        raise
        
        
    
    
def run_train_model():
    
    try:
        
    
        print(
        
            f"Executing: {TRAIN_MODEL_SCRIPT}"
        
        )
    
        execute_python_script(
        
            TRAIN_MODEL_SCRIPT
        
        )
        
        
        print(
            "Task completed successfully"
        )
        
        
    except Exception:
        
        
        raise
    
    

def run_generate_report():
    
    try:
        

        print(
        
            f"Executing: {GENERATE_REPORT_SCRIPT}"
        
        )        


        execute_python_script(
        
            GENERATE_REPORT_SCRIPT
        
        )
        
        
        print(
            "Task completed successfully"
        )


    except Exception:
        
        
        raise
    
    

# ================================
# DAG Configuration
# ================================

with DAG(
        
    dag_id="car_manufacturing_pipeline",
        
    default_args=default_args,
        
    description="Machine Learning pipeline for car manufacturing dataset",
        
    start_date=datetime(2026,7,24),
        
    schedule=None,
        
    catchup=False,
        
        
) as dag:
    
    
    data_cleaning_task = PythonOperator(
        
        task_id="data_cleaning",
        
        python_callable=run_data_cleaning,
        
    ) 


    train_model_task = PythonOperator(
        
        task_id="train_model",
        
        python_callable=run_train_model
    )


    generate_report_task = PythonOperator(
        
        task_id="generate_report",
        
        python_callable=run_generate_report
        
    )
    
    
    # ================================
    # Dependencies
    # ================================

    data_cleaning_task >> train_model_task >> generate_report_task