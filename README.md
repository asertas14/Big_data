# Proyecto de Análisis RFM con Frubana

## Integrantes del Grupo
- Jonnatan Triana
- Juan Carlos Avila
- Jenniffer Escudero
- Andrés Gutierrez H

## Acerca de Frubana
Frubana es una empresa que se dedica a

## Archivos del Repositorio

### 1. `README.md`
Este archivo proporciona una descripción general del proyecto, los integrantes del grupo, una breve introducción sobre Frubana, y una descripción detallada de cada uno de los archivos en este repositorio.

### 2. `preprocesamiento.py` (no funcional por temas de anonimizar clientes por reglas de negocio)
Script en Python que contiene funciones y rutinas para el preprocesamiento y limpieza de los datos. Esto incluye la eliminación de valores atípicos, imputación de valores faltantes, y otras transformaciones necesarias para preparar los datos para el análisis posterior.


### 3. `eda.ipynb`
Notebook de Jupyter que contiene el análisis exploratorio de datos (EDA) realizado sobre el dataset proporcionado. En él se realizan diversas visualizaciones, análisis de estadísticas descriptivas, y se identifican patrones y tendencias en los datos.

### 4. `rfm.ipynb`
Notebook de Jupyter enfocado en el análisis RFM (Recency, Frequency, Monetary). En este archivo se calculan los scores RFM para cada cliente y se realiza una segmentación basada en estos scores para identificar diferentes grupos de clientes y entender su comportamiento.

## Metodología para Construir los Notebooks

1. **Comprensión del Negocio**: Antes de comenzar con cualquier análisis, es fundamental entender el negocio, sus objetivos y las preguntas clave que buscamos responder.
2. **Carga de Datos**: Importamos los datos desde las fuentes correspondientes y realizamos una inspección inicial.
3. **Preprocesamiento**: Utilizando el script `preprocesamiento.py`, limpiamos y transformamos los datos para que estén listos para el análisis cumpliendo las reglas de negocio.
4. **Análisis Exploratorio**: En el notebook `eda.ipynb`, realizamos un análisis profundo para entender la distribución de los datos, identificar patrones y obtener insights.
5. **Modelado**: En el notebook `rfm.ipynb`, aplicamos el análisis RFM para segmentar a los clientes basándonos en su recencia, frecuencia y valor monetario.
6. **Interpretación y Comunicación**: Después de realizar el análisis, interpretamos los resultados y los comunicamos de manera clara y concisa, utilizando visualizaciones y descripciones detalladas.
