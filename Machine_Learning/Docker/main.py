from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import ast

class PredictRequest(BaseModel):
    PULocationID: int
    pickup_weekday: int
    pickup_hour: int

app = FastAPI()

# Cargando datos
df = pd.read_csv('enriched_taxi_data.csv')
adjacent_zones_df = pd.read_csv('adjacent_zones.csv')
adjacent_zones_df['adjacent_zones'] = adjacent_zones_df['adjacent_zones'].apply(ast.literal_eval)
taxi_zones_df = pd.read_csv('taxi_zones.csv')

def get_adjacent_zones(location_id):
    row = adjacent_zones_df.loc[adjacent_zones_df['LocationID'] == location_id]
    if not row.empty:
        return row.iloc[0]['adjacent_zones']
    else:
        return []

# Entrenamiento del modelo
X = df[['PULocationID', 'pickup_weekday', 'pickup_hour']]
y = df['trip_count']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

def predict_demand_with_adjacent(pickup_weekday, pickup_hour, pulocationid):
    adjacent_zones = get_adjacent_zones(pulocationid)
    all_zones = list(set([pulocationid] + adjacent_zones))

    # Preparar datos de entrada
    input_data = pd.DataFrame({
        'PULocationID': all_zones,
        'pickup_weekday': [pickup_weekday] * len(all_zones),
        'pickup_hour': [pickup_hour] * len(all_zones)
    })
    
    # Hacer predicciones
    predictions = model.predict(input_data)
    result = {zone: prediction for zone, prediction in zip(all_zones, predictions)}
    
    # Encontrar zona con mayor demanda
    max_zone = max(result, key=result.get)
    max_demand = result[max_zone]
    zone_name_row = taxi_zones_df.loc[taxi_zones_df['LocationID'] == max_zone]
    max_zone_name = zone_name_row.iloc[0]['zone'] if not zone_name_row.empty else 'Unknown'
    
    # Preparar comparación detallada y limitar a 2 resultados
    comparison = []
    sorted_results = sorted(result.items(), key=lambda x: x[1], reverse=True)
    
    # Tomar las dos mejores zonas
    for zone, demand in sorted_results[:2]:
        zone_row = taxi_zones_df.loc[taxi_zones_df['LocationID'] == zone]
        zone_name = zone_row.iloc[0]['zone'] if not zone_row.empty else 'Unknown'
        comparison.append({
            'zone_id': zone,
            'zone_name': zone_name,
            'predicted_demand': float(demand)  # Convertir a float para la serialización JSON
        })
    
    return {
        "max_zone_id": max_zone,
        "max_zone_name": max_zone_name,
        "demand": float(max_demand),  # Convertir a float para la serialización JSON
        "detailed_comparison": comparison
    }

@app.post("/predict/")
def predict(request: PredictRequest):
    try:
        prediction = predict_demand_with_adjacent(
            pickup_weekday=request.pickup_weekday,
            pickup_hour=request.pickup_hour,
            pulocationid=request.PULocationID
        )
        return prediction
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))