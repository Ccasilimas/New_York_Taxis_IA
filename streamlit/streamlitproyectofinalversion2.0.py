import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import ast

# 🌟 Configuración de la página Streamlit
st.set_page_config(
    page_title="Predicción de Demanda de Taxis",
    page_icon="🚖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 🌟 Colores y estilos personalizados
st.markdown(
    """
    <style>
    .main {
        background-color: #F0F8FF;
        color: #2C3E50;
    }
    .stButton>button {
        color: white;
        background: #3498DB;
        border-radius: 15px;
    }
    .stSlider>div>div>div>div {
        background: #3498DB;
    }
    .stSelectbox>div>div {
        background: #3498DB;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# 🌟 Información del proyecto con iconos y colores
st.title("🚖 Análisis de Viabilidad para Flota de Taxis Ecológicos en Nueva York 🚖")
st.image("https://www.nyc.gov/assets/dca/images/taxi.jpg", use_container_width=True)
st.markdown("""
### 🌱 Green Route Solutions 🌱
#### Innovación en transporte urbano sostenible

🔍 **Objetivo General**
- Asesorar a Urban Transit Corp en la implementación de una flota de taxis ecológicos en Nueva York, optimizando la rentabilidad y reduciendo la huella de carbono.

📊 **Objetivos Específicos**
- **Análisis de Demanda**: Identificar zonas y horarios de alta demanda.
- **Evaluación de Emisiones**: Analizar rutas para reducir consumo de combustible y emisiones.
- **Zonas Óptimas**: Crear un sistema de recomendación que optimice rentabilidad y reducción de emisiones.

👥 **Nuestro Equipo**
- [Camilo Casilimas](https://www.linkedin.com/in/camilo-casilimas/): Arquitecto e Ingeniero de Datos
- [Gustavo Coello](https://www.linkedin.com/in/gustavo-coello-01039b270/): Ingeniero de Datos
- [Alberto Bernal](https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/): Científico de Datos
- [Vera Guillen](https://www.linkedin.com/in/vera-guillen-9b464a303/): Data Analyst
""")

# 🌟 Cargar datos de zonas de taxis
@st.cache_data
def load_zone_data():
    # URL del archivo GeoJSON de zonas de taxis
    zones_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/streamlit/NYC%20Taxi%20Zones.geojson"
    
    # Cargar el archivo GeoJSON
    gdf = gpd.read_file(zones_url)
    return gdf

# Cargar los datos de zonas
zone_gdf = load_zone_data()

# **Crear el mapa de zonas de taxis**
def create_map(gdf):
    # Centro del mapa en Nueva York
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
    
    # Agregar las zonas al mapa
    folium.GeoJson(gdf).add_to(m)
    
    return m

# Crear y mostrar el mapa
taxi_map = create_map(zone_gdf)
st.title("🗺️ Mapa de Zonas de Taxis en Nueva York 🗺️")
st_folium(taxi_map, width=700, height=500)

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
    X = data[['PULocationID', 'pickup_weekday', 'pickup_hour']]  # Cambié a 'pickup_hour' para tener más influencia en la predicción
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
st.title("🔍 Predicción de Demanda de Taxis en NYC 🔍")
st.markdown("Ingrese la hora y la zona para obtener recomendaciones de alta demanda basadas en Machine Learning.")

# **Formulario de entrada con íconos y colores**
st.header("📋 Formulario para Recomendación de Demanda 📋")
with st.form("input_form"):
    pickup_hour = st.slider("🕒 Hora del día (0-23)", min_value=0, max_value=23, value=12)
    pickup_weekday = st.selectbox("📅 Día de la semana", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    pulocation_id = st.number_input("📍 Zona de Recogida (PULocationID)", min_value=1, max_value=255, value=1)
    submit_button = st.form_submit_button("🔍 Obtener Predicción")

# **Si se envía el formulario**
if submit_button:
    weekday_mapping = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
    pickup_weekday_encoded = weekday_mapping[pickup_weekday]
    
    # Predecir demanda
    predicted_demands = predict_demand_with_adjacent(pulocation_id, pickup_weekday_encoded, pickup_hour)
    max_zone = max(predicted_demands, key=predicted_demands.get)
    
    # Mostrar los resultados
    st.write("🚖 Predicción de demanda para la zona seleccionada y sus adyacentes 🚖:")
    st.write(predicted_demands)
    st.markdown(f"### **Zona recomendada con mayor demanda:** {max_zone} (Demanda: {predicted_demands[max_zone]:.2f})")
