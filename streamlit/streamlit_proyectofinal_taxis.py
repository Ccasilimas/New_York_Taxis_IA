import streamlit as st
import pandas as pd
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import ast

# Custom CSS with LinkedIn-inspired styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #f3f2ef;
    }
    
    /* Card styling */
    .css-1r6slb0 {
        background-color: white;
        border-radius: 8px;
        padding: 24px;
        box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
        margin-bottom: 20px;
    }
    
    /* Headers styling */
    h1 {
        color: #000000;
        font-size: 32px !important;
        font-weight: 600 !important;
        margin-bottom: 24px !important;
    }
    
    h2 {
        color: #000000;
        font-size: 24px !important;
        font-weight: 600 !important;
        margin-bottom: 16px !important;
    }
    
    h3 {
        color: #000000;
        font-size: 20px !important;
        font-weight: 600 !important;
        margin-bottom: 12px !important;
    }
    
    /* Links styling */
    a {
        color: #0a66c2 !important;
        text-decoration: none !important;
    }
    
    a:hover {
        text-decoration: underline !important;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #0a66c2;
        color: white;
        border: none;
        border-radius: 24px;
        padding: 10px 24px;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background-color: #004182;
    }
    
    /* Profile card styling */
    .profile-card {
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 16px;
        border: 1px solid #e0e0e0;
    }
    
    /* Stats card styling */
    .stats-card {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        border: 1px solid #e0e0e0;
    }
    
    /* Metric styling */
    .metric-container {
        background-color: white;
        border-radius: 8px;
        padding: 16px;
        margin: 8px 0;
        border: 1px solid #e0e0e0;
    }
    
    .metric-value {
        font-size: 24px;
        font-weight: 600;
        color: #0a66c2;
    }
    
    .metric-label {
        font-size: 14px;
        color: #666666;
    }
    
    /* Form styling */
    .stSelectbox, .stSlider {
        background-color: white;
        border-radius: 4px;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)

# Page configuration
st.set_page_config(
    page_title="NYC Taxi Analysis | Green Route Solutions",
    page_icon="🚖",
    layout="wide"
)

# Header Section
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://www.nyc.gov/assets/dca/images/taxi.jpg", use_container_width=True)

with col2:
    st.title("🚖 Green Route Solutions")
    st.markdown("""
    <div class="profile-card">
        <h3>Sustainable Urban Transport Consultancy</h3>
        <p>New York, United States • Transport & Logistics</p>
        <p>500+ employees • Environmental Services</p>
    </div>
    """, unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="stats-card">
    <h2>About Our Project</h2>
    <p>We're revolutionizing NYC's taxi industry with eco-friendly solutions. Our data-driven approach helps identify optimal zones for sustainable taxi operations while maximizing profitability.</p>
    
    <div style="display: flex; justify-content: space-between; margin-top: 20px;">
        <div class="metric-container" style="flex: 1; margin: 0 10px;">
            <div class="metric-value">255+</div>
            <div class="metric-label">Taxi Zones Analyzed</div>
        </div>
        <div class="metric-container" style="flex: 1; margin: 0 10px;">
            <div class="metric-value">24/7</div>
            <div class="metric-label">Demand Analysis</div>
        </div>
        <div class="metric-container" style="flex: 1; margin: 0 10px;">
            <div class="metric-value">100%</div>
            <div class="metric-label">Eco-Friendly Focus</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Load and cache data functions
@st.cache_data
def load_zone_data():
    zones_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/NYC%20Taxi%20Zones.geojson"
    gdf = gpd.read_file(zones_url)
    return gdf

@st.cache_data
def load_data():
    enriched_data_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/Machine_Learning/enriched_taxi_data.csv"
    adjacent_zones_url = "https://raw.githubusercontent.com/Inclick-me/New_York_Taxis_IA/main/Machine_Learning/adjacent_zones.csv"
    
    enriched_data = pd.read_csv(enriched_data_url)
    adjacent_zones = pd.read_csv(adjacent_zones_url)
    adjacent_zones['adjacent_zones'] = adjacent_zones['adjacent_zones'].apply(ast.literal_eval)
    
    return enriched_data, adjacent_zones

# Load data
zone_gdf = load_zone_data()
df, adjacent_zones_df = load_data()

# Map and Analysis Section
st.markdown("""
<div class="stats-card">
    <h2>Interactive Zone Analysis</h2>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    # Create and display map
    def create_map(gdf):
        m = folium.Map(location=[40.7128, -74.0060], zoom_start=10)
        folium.GeoJson(
            gdf,
            style_function=lambda x: {
                'fillColor': '#0a66c2',
                'color': '#004182',
                'weight': 1,
                'fillOpacity': 0.3
            }
        ).add_to(m)
        return m

    taxi_map = create_map(zone_gdf)
    st_folium(taxi_map, width=700, height=500)

with col2:
    st.markdown("""
    <div class="stats-card">
        <h3>Demand Prediction Tool</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Model training function
    @st.cache_data
    def train_model(data):
        X = data[['PULocationID', 'pickup_weekday', 'pickup_hour']]
        y = data['trip_count']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        return model

    model = train_model(df)

    # Prediction functions
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

    # Input form
    with st.form("prediction_form"):
        pickup_hour = st.slider("🕒 Hour of Day", min_value=0, max_value=23, value=12)
        pickup_weekday = st.selectbox(
            "📅 Day of Week",
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        )
        pulocation_id = st.number_input("📍 Pickup Zone ID", min_value=1, max_value=255, value=1)
        submit_button = st.form_submit_button("Generate Prediction")

    # Display predictions
    if submit_button:
        weekday_mapping = {
            "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3,
            "Friday": 4, "Saturday": 5, "Sunday": 6
        }
        pickup_weekday_encoded = weekday_mapping[pickup_weekday]
        predicted_demands = predict_demand_with_adjacent(pulocation_id, pickup_weekday_encoded, pickup_hour)
        max_zone = max(predicted_demands, key=predicted_demands.get)
        
        st.markdown("""
        <div class="stats-card">
            <h3>Prediction Results</h3>
        </div>
        """, unsafe_allow_html=True)
        
        for zone, demand in predicted_demands.items():
            st.markdown(f"""
            <div class="metric-container">
                <div class="metric-value">Zone {zone}</div>
                <div class="metric-label">Predicted Demand: {demand:.2f}</div>
            </div>
            """, unsafe_allow_html=True)

# Team Section
st.markdown("""
<div class="stats-card">
    <h2>Meet Our Team</h2>
    <div style="display: flex; flex-wrap: wrap; justify-content: space-between;">
        <div class="profile-card" style="flex: 1; min-width: 200px; margin: 10px;">
            <h3>Camilo Casilimas</h3>
            <p>Data Architect & Engineer</p>
            <a href="https://www.linkedin.com/in/camilo-casilimas/">View Profile</a>
        </div>
        <div class="profile-card" style="flex: 1; min-width: 200px; margin: 10px;">
            <h3>Gustavo Coello</h3>
            <p>Data Engineer</p>
            <a href="https://www.linkedin.com/in/gustavo-coello-01039b270/">View Profile</a>
        </div>
        <div class="profile-card" style="flex: 1; min-width: 200px; margin: 10px;">
            <h3>Alberto Bernal</h3>
            <p>Data Scientist</p>
            <a href="https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/">View Profile</a>
        </div>
        <div class="profile-card" style="flex: 1; min-width: 200px; margin: 10px;">
            <h3>Vera Guillen</h3>
            <p>Data Analyst</p>
            <a href="https://www.linkedin.com/in/vera-guillen-9b464a303/">View Profile</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)