## Datasets Utilizados en el Proyecto 🚀
A continuación, presentamos los datasets que emplearemos en nuestro proyecto, junto con una breve descripción de cada uno.

### 1️⃣ Dataset de Medallions Activos en Nueva York 🛺
**Descripción**: Este dataset contiene información sobre los medallions (licencias) activos de los taxis en la ciudad de Nueva York. Incluye detalles como el número de licencia, el número de VIN del vehículo, el tipo de vehículo y el año del modelo.

**Columnas Seleccionadas**: License Number, Vehicle VIN Number, Vehicle Type, Model Year

**Utilidad**:
- Identificar y analizar la composición actual de la flota de taxis.
- Mapear los viajes a vehículos específicos.
- Evaluar el tipo y antigüedad de los vehículos operativos.

### 2️⃣ Dataset de Viajes en Taxis Amarillos y Verdes 🚕
**Descripción**: Este dataset contiene datos detallados de los viajes realizados por taxis amarillos y verdes en Nueva York. Incluye información como la fecha y hora de recogida, ubicaciones de origen y destino, distancia del viaje y monto total.

**Columnas Seleccionadas**: pickup_datetime, PULocationID, DOLocationID, trip_distance, total_amount, passenger_count

**Utilidad**:
- Analizar los patrones de demanda y movilidad en la ciudad.
- Calcular los KPIs definidos, como el número de viajes por zona y hora, ingresos totales por zona y duración promedio del viaje.
- Optimizar la operación de la flota en zonas y horarios de alta demanda.

### 3️⃣ Dataset de Tráfico en Nueva York 🚦
**Descripción**: Este dataset proporciona información sobre los volúmenes de tráfico en diferentes segmentos viales de Nueva York. Incluye datos por distrito, año, mes, día y hora, así como el volumen de tráfico medido en número de vehículos.

**Columnas Seleccionadas**: boro, yr, m, d, HH, vol

**Utilidad**:
- Correlacionar las condiciones del tráfico con los patrones de viaje.
- Optimizar rutas y reducir tiempos de viaje considerando la congestión.
- Mejorar la eficiencia operativa de la flota.

### 4️⃣ Dataset de Vehículos de Combustible Alternativo en EE.UU. ♻️
**Descripción**: Contiene información sobre vehículos que utilizan combustibles alternativos en Estados Unidos. Incluye datos como la categoría del vehículo, modelo, año del modelo, fabricante, tipo de combustible y eficiencia de combustible.

**Columnas Seleccionadas**: Category, Model, Model Year, Manufacturer, Fuel, Alternative Fuel Economy Combined

**Utilidad**:
- Evaluar y comparar la eficiencia de vehículos de combustibles alternativos.
- Informar decisiones sobre la incorporación de vehículos más sostenibles en la flota.
- Analizar el potencial de reducción de emisiones de CO₂.

### 5️⃣ Dataset de Vehículos Eléctricos ⚡
**Descripción**: Este dataset incluye información detallada sobre vehículos eléctricos. Proporciona datos como la marca, modelo, autonomía en kilómetros, eficiencia energética y precio.

**Columnas Seleccionadas**: Brand, Model, Range_Km, Efficiency_WhKm, PriceEuro

**Utilidad**:
- Analizar la viabilidad de integrar vehículos eléctricos en la flota.
- Comparar autonomía y eficiencia para seleccionar los modelos más adecuados.
- Evaluar la inversión necesaria y el potencial ahorro en costos operativos.

### 6️⃣ Dataset de Zonas de Taxis en Nueva York 📍
**Descripción**: Proporciona información sobre las zonas de taxis definidas por la Taxi and Limousine Commission (TLC) en Nueva York. Incluye identificadores de ubicación, distritos y nombres de las zonas.

**Columnas Seleccionadas**: LocationID, Borough, Zone

**Utilidad**:
- Mapear las ubicaciones de origen y destino de los viajes a zonas geográficas específicas.
- Analizar patrones de demanda por zona.
- Facilitar la planificación estratégica y optimización de rutas.
