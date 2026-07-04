# data_cleaning.py

import pandas as pd

# Ruta relativa desde el notebook
file_path = '../datasets/raw/car_manufacturing_data.csv'
df = pd.read_csv(file_path)

# Guardar copia del dataset original
df_original = df.copy()

# Eliminar duplicados, conservando el primer  registro según el índice
df = df.drop_duplicates(subset=['Car_ID', 'Production_Date'], keep='first')

# Eliminar filas con Cost nulo
df = df.dropna(subset=['Cost'])

# Guardar conjunto de datos limpios.
df.to_csv('../datasets/processed/car_manufacturing_clean.csv', index=False)


# Validación rápida
expected_rows = 90
actual_rows = df.shape[0]

if actual_rows != expected_rows:
    print(f"⚠️ Atención: se esperaban {expected_rows} filas, pero obtuvimos {actual_rows}")
else:
    print(f"✅ Conjunto de datos limpio con {actual_rows} filas")