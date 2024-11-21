import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import ast

# 🌟 Configuración de la página Streamlit (debe ser lo primero)
st.set_page_config(
    page_title="Predicción de Demanda de Taxis",
    page_icon="🚖",
    layout="wide"
)

# 🌟 Información del proyecto
st.image("https://example.com/taxis_ny_image.jpg", use_column_width=True)  # Sustituir URL con una imagen relevante de taxis en Nueva York
st.title("Análisis de Viabilidad para Flota de Taxis Ecológicos en Nueva York")
st.markdown("""
### Green Route Solutions
Somos una consultora especializada en soluciones sostenibles para el transporte urbano. Nuestro proyecto evalúa la viabilidad de implementar una nueva flota de taxis ambientalmente amigables en Nueva York.

#### Objetivo General
Asesorar a Urban Transit Corp en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en Nueva York, identificando las mejores zonas para iniciar el negocio.

#### Objetivos Específicos
- **Análisis de Demanda**: Identificar zonas y horarios de alta demanda.
- **Evaluación de Emisiones**: Analizar rutas para reducir consumo de combustible y emisiones.
- **Zonas Óptimas**: Crear un sistema de recomendación que optimice rentabilidad y reducción de emisiones.

#### Nuestro Equipo
- **Camilo Casilimas**: Arquitecto e Ingeniero de Datos
- **Gustavo Coello**: Ingeniero de Datos
- **Alberto Bernal**: Científico de Datos
- **Vera Guillen**: Data Analyst
""", unsafe_allow_html=True)

# 🌟 Cargar datos desde GitHub
@st.cache_data
def load_data():
    # URLs crudas de los archivos en GitHub
    enriched_data_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/Machine_Learning/enriched_taxi_data.csv"
    adjacent_zones_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/Machine_Learning/adjacent_zones.csv"
    
    # Cargar los datos desde las URLs
    enriched_data = pd.read_csv(enriched_data_url)
    adjacent_zones = pd.read_csv(adjacent_zones_url)
    
    # Convertir la columna `adjacent_zones` a listas de Python
    adjacent_zones['adjacent_zones'] = adjacent_zones['adjacent_zones'].apply(ast.literal_eval)
    
    return enriched_data, adjacent_zones

# Cargar los datos
df, adjacent_zones_df = load_data()

# **Entrenar el modelo de regresión lineal**
@st.cache_data
def train_model(data):
    # Seleccionar las características (X) y el objetivo (y)
    X = data[['PULocationID', 'pickup_weekday', 'pickup_hour']]
    y = data['trip_count']
    
    # Dividir los datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Inicializar y entrenar el modelo
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model

# Entrenar el modelo
model = train_model(df)

# **Obtener zonas adyacentes**
def get_adjacent_zones(location_id):
    row = adjacent_zones_df.loc[adjacent_zones_df['LocationID'] == location_id]
    if not row.empty:
        return row.iloc[0]['adjacent_zones']
    else:
        return []

# **Predecir demanda con zonas adyacentes**
def predict_demand_with_adjacent(location_id, pickup_weekday, pickup_hour):
    adjacent_zones = get_adjacent_zones(location_id)
    all_zones = adjacent_zones + [location_id]
    input_data = pd.DataFrame({
        'PULocationID': all_zones,
        'pickup_weekday': [pickup_weekday] * len(all_zones),
        'pickup_hour': [pickup_hour] * len(all_zones)
    })
    predictions = model.predict(input_data)
    result = {zone: prediction for zone, prediction in zip(all_zones, predictions)}
    return result

# **Título y descripción**
st.title("🚖 Predicción de Demanda de Taxis en NYC")
st.markdown("<span style='color:blue'>Ingrese la hora y la zona para obtener recomendaciones de alta demanda basadas en Machine Learning.</span>", unsafe_allow_html=True)

# **