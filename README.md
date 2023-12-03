# Proyecto de Final Big Data Frubana

## Integrantes del Grupo
- Jonnatan Triana
- Juan Carlos Avila
- Jenniffer Escudero
- Andrés Gutierrez H

## Acerca de Frubana
Frubana es una  empresa de alimentos que utiliza tecnología e innovación en logística para conectar directamente a agricultores y consumidores. La misión de Frubana es hacer la comida de Latinoamérica más barata y ser el servicio “todo en uno” de los restaurantes de la región. 

Fundada en 2018 con operación en tres países (Colombia, Brasil, México), Frubana se ha convertido en poco tiempo en una empresa altamente escalable con alto capital de inversión por parte de fondos especializados. Actualmente la compañía cuenta con operación en 10 ciudades de Colombia, México y Brasil, y cuenta con inversión de cerca de 270 millones de dólares por parte de diferentes grupos inversionistas. Atiende a cerca de 35.000 clientes y cuenta con un equipo de cerca de 1.000 personas en oficinas y 4.000 en bodegas 

## Archivos del Repositorio

1) Carpeta de Informe: Carpeta que contiene las presentaciones ejecutivas del proyecto y los documentos formales.
   La entrega 3 corresponde al archivo Informe/Proyecto Final Entrega 3.pdf

2) Carpeta de Notebooks: Carpeta que contiene los cuadernos con el código trabajado. Existe a saber:
   -churn_statics.ipynb
   -eda.ipynb
   -predictor.ipynb
   -preprocesamiento.ipynb
   -rfm.ipynb

3) Carpeta de Data: Datos proporcionados por el negocio para satisfacer el abordaje del proyecto.

## Metodología para Construir los Notebooks

1. **Comprensión del Negocio**: Antes de comenzar con cualquier análisis, es fundamental entender el negocio, sus objetivos y las preguntas clave que buscamos responder.
2. **Carga de Datos**: Importamos los datos desde las fuentes correspondientes y realizamos una inspección inicial.
3. **Preprocesamiento**: Utilizando el script `preprocesamiento.py`, limpiamos y transformamos los datos para que estén listos para el análisis cumpliendo las reglas de negocio.
4. **Análisis Exploratorio**: En el notebook `eda.ipynb`, realizamos un análisis profundo para entender la distribución de los datos, identificar patrones y obtener insights.
5. **Modelado**: En el notebook `rfm.ipynb`, aplicamos el análisis RFM para segmentar a los clientes basándonos en su recencia, frecuencia y valor monetario.
6. **Interpretación y Comunicación**: Después de realizar el análisis, interpretamos los resultados y los comunicamos de manera clara y concisa, utilizando visualizaciones y descripciones detalladas.
