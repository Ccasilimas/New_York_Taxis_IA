import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from dotenv import load_dotenv
import os
import numpy as np

# 🌟 Cargar variables de entorno para la conexión a la base de datos
load_dotenv()

# 🔐 Configuración de la conexión a la base de datos
DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT", 3306)),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME")
}

# Crear el motor de SQLAlchemy para conectarse a la base de datos
engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# 🌟 Configuración de la página Streamlit
st.set_page_config(
    page_title="Recomendación de Rutas de Taxis en Nueva York",
    page_icon="🚖",
    layout="wide"
)

# Título
st.title("🚖 Recomendación de Rutas para Conductores de Taxis en Nueva York")

# **Objetivos del Proyecto**
st.header("Objetivos del Proyecto")
st.markdown("""
Este proyecto tiene como objetivo desarrollar un sistema de recomendación para conductores de taxis en Nueva York, basado en el análisis de datos históricos de viajes. Los objetivos principales son:
- **Optimización de rutas**: Ayudar a los conductores a tomar las mejores decisiones sobre qué ruta seguir según el tráfico y la demanda de taxis.
- **Mejora en la eficiencia**: Reducir el tiempo de inactividad y aumentar los ingresos de los conductores.
- **Análisis predictivo**: Predecir la cantidad de viajes en diferentes zonas de la ciudad en función de la hora, el día y la zona de recogida.
""")

# **Equipo de Trabajo**
st.header("Equipo de Trabajo")
st.markdown("""
El proyecto fue desarrollado por el siguiente equipo:
- **Nombre 1**: Data Scientist
- **Nombre 2**: Desarrollador de Backend
- **Nombre 3**: Especialista en Big Data
- **Nombre 4**: Ingeniero de Machine Learning
""")

# **Descripción del Modelo de Machine Learning**
st.header("Modelo de Machine Learning")
st.markdown("""
El modelo utilizado para realizar las recomendaciones es un modelo de **regresión lineal**, entrenado con datos históricos de viajes de taxis en Nueva York. Utiliza las siguientes características:
- **PULocationID**: Código de la zona de recogida del taxi.
- **pickup_borough**: Barrio de la recogida.
- **pickup_day**: Día de la semana.
- **pickup_hour**: Hora de la recogida.

El modelo predice la cantidad de viajes que se espera para una zona dada en un determinado momento del día.
""")

# **Datos**
st.header("Datos")
st.markdown("""
Los datos utilizados en el proyecto provienen de una base de datos MySQL, y contienen información histórica sobre los viajes de taxis en Nueva York. Los datos incluyen detalles como:
- Fecha y hora de recogida
- Ubicación del viaje
- Número de viajes realizados
- Información de las zonas y barrios

### Ejemplo de los primeros registros:
""")

# Conexión a la base de datos y carga de datos
query = "SELECT * FROM enriched_taxi_data LIMIT 10"
df = pd.read_sql(query, engine)
st.write(df)

# **Formulario de Entrada para los Conductores**
st.header("Formulario para Recomendación de Ruta")
st.markdown("""
Por favor, ingrese los siguientes datos para obtener la recomendación de la mejor ruta.
""")

# Entradas del usuario
with st.form("input_form"):
    hora = st.slider("Hora del día (0-23)", min_value=0, max_value=23, value=12)
    zona = st.number_input("Zona de Recogida (PULocationID)", min_value=1, max_value=255, value=1)
    barrio = st.selectbox("Barrio de Recogida", ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"])
    dia = st.selectbox("Día de la Semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])

    submit_button = st.form_submit_button("Obtener Recomendación")

# Si el formulario es enviado
if submit_button:
    # Convertir el barrio a variable dummy
    barrio_dict = {"Manhattan": 1, "Brooklyn": 2, "Queens": 3, "Bronx": 4, "Staten Island": 5}
    barrio_encoded = barrio_dict.get(barrio, 0)

    # Crear el DataFrame para la predicción
    input_data = pd.DataFrame({
        'PULocationID': [zona],
        'pickup_borough': [barrio_encoded],
        'pickup_day': [dia],
        'pickup_hour': [hora]
    })

    # Convertir la variable categórica 'pickup_borough' en variables dummy
    input_data = pd.get_dummies(input_data, columns=['pickup_borough'], drop_first=True)

    # Realizar la predicción (aquí cargaríamos el modelo si está previamente entrenado)
    model = LinearRegression()
    model.fit(df[['PULocationID', 'pickup_borough', 'pickup_day', 'pickup_hour']], df['trip_count'])

    prediction = model.predict(input_data)

    # Mostrar la recomendación
    st.write(f"Predicción de la cantidad de viajes: {prediction[0]}")
    st.markdown("Con esta información, recomendamos dirigirse a la zona con mayor demanda.")

