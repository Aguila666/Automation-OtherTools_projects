# datasets/generate_dataset.py
import pandas as pd
import numpy as np
import os

def create_car_dataset():
    """
    Generates a simulated car manufacturing dataset with:
    - 100 cars
    - Columns: Car_ID, Production_Date, Engine_Type, Production_Line, Cost, Defects
    - Includes missing values, duplicates, and outliers
    Saves the dataset as 'car_manufacturing_data.csv' in the same folder as this script.
    Returns the DataFrame.
    """
    # Simulate a dataset for car production
    np.random.seed(42)

    data = {
        'Car_ID': [f'CAR{str(i).zfill(4)}' for i in range(1, 101)],
        'Production_Date': pd.date_range('2021-01-01', periods=100, freq='D'),
        'Engine_Type': np.random.choice(['V6', 'V8', 'Electric'], 100),
        'Production_Line': np.random.choice(['Line 1', 'Line 2', 'Line 3'], 100),
        'Cost': np.random.uniform(20000, 50000, 100),
        'Defects': np.random.randint(0, 5, 100)
    }

    df = pd.DataFrame(data)

    # Simulate missing values, duplicates, and outliers
    df.loc[::10, 'Cost'] = np.nan  # Missing values
    df = pd.concat([df, df.sample(10)], ignore_index=True)  # Duplicates
    df.loc[::5, 'Cost'] = df['Cost'] * 1.5  # Outliers

    # Save to CSV in the same folder as this script
    data_path = os.path.join(os.path.dirname(__file__), "car_manufacturing_data.csv")
    df.to_csv(data_path, index=False)

    return df

# Optional: allow running script directly
if __name__ == "__main__":
    create_car_dataset()