# breast-mass-data
Describen las características de los núcleos celulares presentes en la imagen de una masa mamaria.

Análisis Predictivo de Cáncer de Mama
Descripción del Proyecto
Este proyecto tiene como objetivo desarrollar un modelo de clasificación binaria para predecir si una muestra de tejido mamario es benigna o maligna basado en sus características. Se ha trabajado con un dataset derivado de imágenes de aspiración con aguja fina (PAAF) para analizar y procesar las características relacionadas con el cáncer de mama, asegurando una adecuada preparación de los datos para el modelado predictivo.
Estructura del Proyecto
El flujo del proyecto sigue la metodología CRISP-DM (Cross Industry Standard Process for Data Mining) y se organiza en los siguientes pasos:
1.	Obtención del Dataset:
o	El dataset inicial incluye características relacionadas con el tamaño, la textura, la forma y las propiedades de los núcleos celulares, calculadas en tres dimensiones: promedio (mean), error estándar (SE) y peor caso (worst).
o	Variable objetivo: diagnostico (maligno = 1, benigno = 0).
2.	Exploratory Data Analysis (EDA):
o	Realización de análisis estadísticos y visuales para identificar patrones y diferencias entre las clases maligno y benigno.
o	Identificación de características con baja o nula correlación con el diagnóstico para evaluación y posible exclusión.
3.	Data Wrangling (Limpieza y Transformación):
o	Eliminación de valores duplicados y nulos.
o	Traducción y estandarización de nombres de columnas a español.
o	Conversión de la variable diagnostico a formato binario (1 = maligno, 0 = benigno).
o	Resolución del desbalanceo de clases (357 benignos, 212 malignos) mediante técnicas como sobremuestreo, submuestreo o SMOTE.
o	Escalado y normalización de características para algoritmos que lo requieren.
4. Feature Engineering
o	Verificación de variables y su correlación el target.
5. Modeling
o	Funciones para probar regresion logistica, arbol de decisión y random forest
o	Registro historico de los modelos para hacer graficas y visualizar el desempeño de los modelos
Instrucciones de Uso
Requisitos
•	Lenguaje y Librerías: 
o	Python 3.x
o	Librerías necesarias: pandas, numpy, seaborn, matplotlib, scikit-learn, imblearn
•	Dataset: El archivo debe estar en formato .csv y ubicado en el directorio raíz del proyecto.
Instalación
1.	Clona este repositorio en tu máquina local: 
2.	git clone https://github.com/adnacato/breast-mass-data.git
3.	Instala las dependencias requeridas ejecutando: 
4.	pip install -r requirements.txt
Ejecución
1.	Carga el archivo del dataset en el directorio principal del proyecto.
2.	Ejecuta los notebooks en orden: 
o	EDA.ipynb: Exploración de datos y análisis inicial.
o	Data_Wrangling.ipynb: Limpieza y preparación de los datos para el modelo.
3.	Visualiza los resultados y métricas generadas.
Resultados Esperados
El objetivo del modelo es clasificar las muestras con una alta precisión, identificando correctamente los casos malignos para facilitar un diagnóstico temprano y mejorar la toma de decisiones en contextos clínicos.
________________________________________
Contribuciones
Si deseas colaborar en este proyecto, eres bienvenido/a. Por favor, realiza un fork de este repositorio y envía tus sugerencias a través de un pull request.
________________________________________
Autor/a
Aurora
Ubicación: Quito, Ecuador
________________________________________
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.

