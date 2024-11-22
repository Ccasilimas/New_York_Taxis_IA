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

# 🌟 Estilos personalizados con un enfoque moderno y corporativo
st.markdown(
    """
    <style>
    .main {
        background-color: #f5fff7;
        font-family: 'Helvetica', sans-serif;
    }
    h1, h2, h3, h4 {
        color: #2C3E50;
    }
    .stButton>button {
        color: white;
        background: linear-gradient(to right, #27AE60, #2ECC71);
        border-radius: 12px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        transition: background 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background: linear-gradient(to right, #2ECC71, #27AE60);
    }
    .stSlider>div>div>div>div {
        background: #27AE60;
    }
    .stSelectbox>div>div {
        background: #EAFDEA;
        border-radius: 10px;
    }
    .stForm {
        background-color: #ffffff;
        padding: 20px;
        border: 1px solid #d5e5d5;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True
)

# 🌟 Título y descripción principal
st.title("🚖 Análisis de Viabilidad para Flota de Taxis Ecológicos 🚖")
st.image(
    "https://www.nyc.gov/assets/dca/images/taxi.jpg",
    use_container_width=True,
    caption="Nueva York: Innovación en transporte urbano sostenible"
)
st.markdown("""
### 🌍 **Green Route Solutions**
#### 🌱 Tecnología al servicio de la sostenibilidad 🌱
Optimización de transporte urbano para reducir huella de carbono y maximizar rentabilidad.
""")

# 🌟 Cargar datos geográficos y mapa interactivo
@st.cache_data
def load_zone_data():
    zones_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/streamlit/NYC%20Taxi%20Zones.geojson"
    gdf = gpd.read_file(zones_url)
    return gdf

zone_gdf = load_zone_data()

def create_map(gdf):
    m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
    folium.GeoJson(gdf, style_function=lambda x: {
        'fillColor': '#2ECC71',
        'color': '#27AE60',
        'weight': 1
    }).add_to(m)
    return m

st.subheader("🗺️ **Mapa de Zonas de Taxis en Nueva York**")
taxi_map = create_map(zone_gdf)
st_folium(taxi_map, width=800, height=500)

# 🌟 Cargar y preparar datos
@st.cache_data
def load_data():
    enriched_data_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/Machine_Learning/enriched_taxi_data.csv"
    adjacent_zones_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/Machine_Learning/adjacent_zones.csv"
    enriched_data = pd.read_csv(enriched_data_url)
    adjacent_zones = pd.read_csv(adjacent_zones_url)
    adjacent_zones['adjacent_zones'] = adjacent_zones['adjacent_zones'].apply(ast.literal_eval)
    return enriched_data, adjacent_zones

df, adjacent_zones_df = load_data()

@st.cache_data
def train_model(data):
    X = data[['PULocationID', 'pickup_weekday', 'pickup_hour']]
    y = data['trip_count']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

model = train_model(df)

def get_adjacent_zones(location_id):
    row = adjacent_zones_df.loc[adjacent_zones_df['LocationID'] == location_id]
    return row.iloc[0]['adjacent_zones'] if not row.empty else []

def predict_demand_with_adjacent(location_id, pickup_weekday, pickup_hour):
    adjacent_zones = get_adjacent_zones(location_id)
    all_zones = adjacent_zones + [location_id]
    input_data = pd.DataFrame({
        'PULocationID': all_zones,
        'pickup_weekday': [pickup_weekday] * len(all_zones),
        'pickup_hour': [pickup_hour] * len(all_zones)
    })
    predictions = model.predict(input_data)
    return {zone: prediction for zone, prediction in zip(all_zones, predictions)}

# 🌟 Formulario de entrada
st.header("🔍 **Predicción de Demanda**")
st.markdown("### Ingrese los parámetros para obtener predicciones de demanda en tiempo real.")
with st.form("input_form", clear_on_submit=True):
    pickup_hour = st.slider("🕒 Seleccione la hora (0-23)", 0, 23, 12)
    pickup_weekday = st.selectbox("📅 Seleccione el día", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
    pulocation_id = st.number_input("📍 ID de Zona (1-255)", 1, 255, step=1)
    submitted = st.form_submit_button("🔍 Predecir Demanda")

if submitted:
    weekday_mapping = {"Lunes": 0, "Martes": 1, "Miércoles": 2, "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
    pickup_weekday_encoded = weekday_mapping[pickup_weekday]
    predicted_demands = predict_demand_with_adjacent(pulocation_id, pickup_weekday_encoded, pickup_hour)
    max_zone = max(predicted_demands, key=predicted_demands.get)
    
    st.success(f"🚖 Zona de mayor demanda: **{max_zone}** con una predicción de **{predicted_demands[max_zone]:.2f}** viajes.")
    st.write("🔍 **Predicción detallada por zonas**:")
    st.json(predicted_demands)
