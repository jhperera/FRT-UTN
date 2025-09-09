import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import altair as alt

# --- Estilos CSS personalizados ---
st.markdown("""
<style>
/* Estilo del cuerpo de la página */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: #f0f2f6; /* Color de fondo gris claro */
    color: #333333; /* Color de texto oscuro */
}

/* Estilo para los títulos */
.stTitle, .stHeader {
    color: #4CAF50; /* Verde brillante para los títulos */
    text-align: center;
    font-weight: bold;
}

/* Estilo para las solapas */
.stTabs [data-baseweb="tab-list"] {
    gap: 24px;
}

.stTabs [data-baseweb="tab"] {
    height: 50px;
    white-space: pre-wrap;
    background-color: #f0f2f6;
    border-radius: 4px 4px 0px 0px;
    gap: 12px;
    padding-top: 10px;
    padding-bottom: 10px;
    font-size: 18px;
    font-weight: bold;
    color: #777777;
}

.stTabs [aria-selected="true"] {
    background-color: #ffffff;
    color: #000000;
}

/* Contenedores de elementos */
.block-container {
    padding-top: 30px;
    padding-bottom: 30px;
    padding-left: 20px;
    padding-right: 20px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Sombra suave */
    margin-bottom: 20px;
}

/* Estilo de los controles (slider, selectbox, checkbox) */
.stSlider label, .stSelectbox label, .stCheckbox label {
    font-size: 16px;
    font-weight: bold;
    color: #555555;
}

.stSlider [role="slider"] {
    background-color: #4CAF50;
}

.stSelectbox {
    border-radius: 8px;
}

.stCheckbox span {
    color: #555555;
}

/* Estilo para los gráficos de Plotly */
.plotly-graph-div {
    border-radius: 10px;
    overflow: hidden; /* Oculta los bordes del gráfico que se salgan */
}
</style>
""", unsafe_allow_html=True)
# --- Fin de Estilos CSS ---

# Título de la aplicación
st.title('Aplicación Interactiva con Solapas y Gráficos')

# Creación de las solapas
tab1, tab2, tab3 = st.tabs(["Gráfico de Líneas", "Gráfico de Barras", "Gráfico de Dispersión"])

# Datos de ejemplo (inventados)
@st.cache_data
def get_data():
    """Genera datos aleatorios para la aplicación."""
    df_line = pd.DataFrame({
        'año': [2021, 2022, 2023, 2024, 2025],
        'ventas': np.random.randint(100, 500, 5)
    })
    df_bar = pd.DataFrame({
        'categoría': ['A', 'B', 'C', 'D', 'E'],
        'ingresos': np.random.randint(50, 200, 5)
    })
    df_scatter = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100)
    })
    return df_line, df_bar, df_scatter

df_line, df_bar, df_scatter = get_data()

# ---

### **Pestaña 1: Gráfico de Líneas con Plotly**

with tab1:
    st.header('Gráfico de Líneas con Plotly')

    # Deslizador para filtrar datos
    max_ventas = st.slider('Filtrar por ventas máximas', min_value=100, max_value=500, value=500)

    # Filtrar el dataframe
    filtered_df_line = df_line[df_line['ventas'] <= max_ventas]

    # Crear el gráfico con Plotly
    fig_line = px.line(filtered_df_line, x='año', y='ventas',
                       title='Ventas Anuales')
    st.plotly_chart(fig_line, use_container_width=True)

# ---

### **Pestaña 2: Gráfico de Barras con Plotly**

with tab2:
    st.header('Gráfico de Barras con Plotly')

    # Selector de categorías
    categoria_seleccionada = st.selectbox('Selecciona una categoría', options=df_bar['categoría'].unique())

    # Filtrar el dataframe
    filtered_df_bar = df_bar[df_bar['categoría'] == categoria_seleccionada]

    # Crear el gráfico con Plotly
    fig_bar = px.bar(filtered_df_bar, x='categoría', y='ingresos',
                     title=f'Ingresos de la categoría {categoria_seleccionada}')
    st.plotly_chart(fig_bar, use_container_width=True)

# ---

### **Pestaña 3: Gráfico de Dispersión con Altair**

with tab3:
    st.header('Gráfico de Dispersión con Altair')

    # Checkbox para mostrar/ocultar los puntos
    mostrar_puntos = st.checkbox('Mostrar puntos', value=True)

    if mostrar_puntos:
        # Crea el gráfico de dispersión con Altair
        chart = alt.Chart(df_scatter).mark_circle().encode(
            x='x',
            y='y'
        ).properties(
            title='Gráfico de Dispersión'
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("Gráfico oculto. Marca la casilla para mostrarlo.")
