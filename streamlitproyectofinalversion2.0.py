import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine
import ast
from dotenv import load_dotenv
import os

# 🌟 Cargar variables de entorno
load_dotenv()

# 🔐 Configuración de la conexión a la base de datos
DB_CONFIG = {
    'host': os.getenv("DB_HOST"),
    'port': int(os.getenv("DB_PORT", 3306)),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME")
}

# Crear el motor de SQLAlchemy
engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# 🌟 Configuración de la página Streamlit
st.set_page_config(
    page_title="Predicción de Demanda de Taxis",
    page_icon="🚖",
    layout="wide"
)

# **Título y Descripción**
st.title("🚖 Predicción de Demanda de Taxis en NYC")
st.markdown("Ingrese la hora y la zona para obtener recomendaciones de alta demanda basadas en Machine Learning.")

# **Cargar datos**
@st.cache_data
def load_data():
    enriched_data = pd.read_sql("SELECT * FROM enriched_taxi_data", engine)
    adjacent_zones = pd.read_csv("adjacent_zones.csv")
    adjacent_zones['adjacent_zones'] = adjacent_zones['adjacent_zones'].apply(ast.literal_eval)
    return enriched_data, adjacent_zones

df, adjacent_zones_df = load_data()

# Entrenar modelo
@st.cache_data
def train_model(data):
    X = data[['PULocationID', 'pickup_weekday', 'pickup_hour']]
    y = data['trip_count']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

model = train_model(df)

# Obtener zonas adyacentes
def get_adjacent_zones(location_id):
    row = adjacent_zones_df.loc[adjacent_zones_df['LocationID'] == location_id]
    if not row.empty:
        return row.iloc[0]['adjacent_zones']
    else:
        return []

# Predecir demanda con zonas adyacentes
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

# **Formulario de entrada**
st.header("Formulario para Recomendación de Demanda")
with st.form("input_form"):
    pickup_hour = st.slider("Hora del día (0-23)", min_value=0, max_value=23, value=12)
    pickup_weekday = st.selectbox("Día de la semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    pulocation_id = st.number_input("Zona de Recogida (PULocationID)", min_value=1, max_value=255, value=1)
    submit_button = st.form_submit_button("Obtener Predicción")

# Si se envía el formulario
if submit_button:
    weekday_mapping = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
    pickup_weekday_encoded = weekday_mapping[pickup_weekday]
    
    # Predecir demanda
    predicted_demands = predict_demand_with_adjacent(pulocation_id, pickup_weekday_encoded, pickup_hour)
    max_zone = max(predicted_demands, key=predicted_demands.get)
    
    st.write(f"Predicción de demanda para la zona seleccionada y sus adyacentes:")
    st.write(predicted_demands)
    st.markdown(f"### **Zona recomendada con mayor demanda:** {max_zone} (Demanda: {predicted_demands[max_zone]:.2f})")

