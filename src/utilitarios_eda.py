# archivo: utilitarios_eda.py

from sklearn.ensemble import IsolationForest

def detectar_outliers_isolation_forest(data, contamination=0.05, random_state=42):
    """
    Detecta outliers usando el modelo Isolation Forest.

    Parámetros:
    - data: DataFrame o array con los datos.
    - contamination: proporción estimada de outliers.
    - random_state: semilla para reproducibilidad.

    Retorna:
    - outlier_labels: array con etiquetas (1 = normal, -1 = outlier)
    - outliers: subconjunto del DataFrame original con los outliers
    """
    iso_forest = IsolationForest(contamination=contamination, random_state=random_state)
    outlier_labels = iso_forest.fit_predict(data)
    outliers = data[outlier_labels == -1]
    return outlier_labels, outliers
