# Resumen del análisis

## Descripción General del conjunto de datos

El dataset original contenía 110 registros y 6 columnas. De estas columnas, cinco contenían información categórica y una (Cost) contenía información numérica (float64).

Durante la exploración inicial se identificó que únicamente la columna Cost presentaba valores nulos (11 registros). Las demás columnas no contenían valores faltantes.

## Notas relacionadas a la limpieza de los datos

Como parte del proceso de limpieza, se verificó la existencia de valores nulos, registros duplicados, posibles valores atípicos y valores únicos en cada columna.

Se identificaron 10 registros duplicados en las columnas Car_ID y Production_Date. Debido a que la mayoría de la información asociada a dichos registros era idéntica, se decidió conservar únicamente la primera ocurrencia de cada duplicado.

Posteriormente, se eliminaron los registros con valores nulos en la columna Cost.

Para la fase de modelado se excluyeron las columnas Car_ID y Production_Date, ya que se consideró que aportaban poca información relevante para la predicción de la variable objetivo.

Tras el proceso de limpieza, el conjunto de datos quedó conformado por 90 registros válidos.

## Resultados de los modelos

Se utilizó inicialmente un modelo de Regresión Lineal para predecir la variable objetivo Cost.

Los resultados obtenidos fueron:

MSE: 111,890,588.62
R²: 0.0036

Estos resultados indican que el modelo posee una capacidad predictiva muy limitada sobre la variable objetivo.

Con el objetivo de validar si un modelo no lineal podía capturar patrones adicionales en los datos, se entrenó un modelo Random Forest Regressor.

MSE: 139,743,198.06
R²: -0.2445

El desempeño del modelo Random Forest fue incluso inferior al obtenido por la Regresión Lineal.

Adicionalmente, se realizó un análisis de correlación entre las variables predictoras y la variable objetivo Cost. La correlación más alta observada fue aproximadamente del 9 %, lo que sugiere una relación débil entre las variables disponibles y la variable objetivo.

## conclusiones

Los resultados obtenidos indican que las variables disponibles poseen una capacidad limitada para explicar la variabilidad de la variable Cost.

Ninguna de las variables utilizadas mostró una correlación significativa con la variable objetivo. Asimismo, tanto el modelo lineal como el modelo no lineal presentaron métricas de desempeño deficientes.

Otro factor relevante es el tamaño reducido del conjunto de datos, que después del proceso de limpieza quedó compuesto por únicamente 90 registros.

Finalmente, solo una de las variables predictoras (Defects) era numérica y presentó una correlación inferior al 7 % con la variable objetivo, lo que contribuye a explicar el bajo desempeño observado en ambos modelos.

## Siguientes pasos

- Automatizar el flujo de trabajo con Apache Airflow para generar los modelos y métricas automáticamente.
- Explorar la visualización de métricas y resultados usando Power BI.
- Considerar la generación de features adicionales o la obtención de más datos para mejorar la predicción.