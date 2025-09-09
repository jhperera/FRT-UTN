# 1. Importar las bibliotecas necesarias
import streamlit as st
import pandas as pd
import numpy as np

# 2. Configurar el título de la página y otros elementos
st.title('Mi primera aplicación con Streamlit 🎈')
st.write('Esta es una aplicación interactiva que muestra datos aleatorios.')

# 3. Crear datos simulados
# Usamos un slider para que el usuario pueda elegir la cantidad de datos
num_puntos = st.slider('Selecciona el número de puntos:', 10, 100, 50)
st.write(f"Mostrando {num_puntos} puntos de datos.")

# Generamos datos aleatorios para un DataFrame de Pandas
data = pd.DataFrame(
    np.random.randn(num_puntos, 2),  # Genera una matriz de números aleatorios
    columns=['col1', 'col2']  # Nombres de las columnas
)

# 4. Visualizar los datos
# Usamos un gráfico de dispersión (scatter chart) para ver la distribución de los datos
st.subheader('Gráfico de los datos')
st.scatter_chart(data)

# 5. Mostrar el DataFrame completo
st.subheader('Tabla de los datos')
st.dataframe(data)