# Descripción y Utilidad de los Datasets del Proyecto

## 1. Dataset de Especificaciones de Vehículos de Gasolina
**Descripción del Contenido**: Este dataset contiene información detallada sobre las especificaciones de vehículos que utilizan gasolina. Incluye datos como el año del modelo, el fabricante, el modelo, la eficiencia de combustible combinada y las emisiones de CO₂.

**Columnas Incluidas**:
- **Year**: Año del modelo del vehículo.
- **Manufacturer**: Fabricante del vehículo.
- **Model**: Modelo del vehículo.
- **fuelType**: Tipo de combustible (Gasolina).
- **comb08**: Eficiencia de combustible combinada.
- **co2**: Emisiones de CO₂.

**Utilidad del Dataset**:
- **Análisis de Eficiencia**: Evaluar la eficiencia de los vehículos de gasolina en comparación con los vehículos eléctricos.
- **Emisiones de CO₂**: Comparar las emisiones de CO₂ de los vehículos de gasolina con las de los vehículos eléctricos para analizar el impacto ambiental.
- **Optimización de Flota**: Ayudar a determinar qué vehículos de gasolina pueden ser reemplazados por eléctricos para mejorar la sostenibilidad.

## 2. Dataset de Medallions Activos en Nueva York
**Descripción del Contenido**: Este dataset contiene información sobre los medallions activos en Nueva York, que representan licencias de operación para taxis. Incluye detalles como el número de licencia, el número de VIN del vehículo, el tipo de vehículo y el año del modelo.

**Columnas Incluidas**:
- **License Number**: Número de licencia del medallón.
- **Vehicle VIN Number**: Número de Identificación del Vehículo (VIN).
- **Vehicle Type**: Tipo de vehículo (por ejemplo, eléctrico, híbrido).
- **Model Year**: Año del modelo del vehículo.
- **Last Date Updated**: Fecha de la última actualización de la información.
- **Last Time Updated**: Hora de la última actualización de la información.

**Utilidad del Dataset**:
- **Identificación de Vehículos**: Permitir el mapeo de viajes a vehículos específicos mediante el número de licencia y VIN.
- **Análisis de Flota**: Evaluar la composición de la flota de taxis en términos de tipos y años de vehículos.
- **Actualización de Datos**: Mantener actualizada la base de datos con información relevante sobre los vehículos operativos.

## 3. Dataset de Viajes en Taxis Amarillos y Verdes
**Descripción del Contenido**: Este dataset contiene datos de viajes realizados por taxis amarillos y verdes en Nueva York. Incluye información detallada sobre cada viaje, como la fecha y hora de recogida, la ubicación de recogida y destino, la distancia del viaje, el número de pasajeros y el monto total del viaje.

**Columnas Incluidas**:
- **pickup_datetime**: Fecha y hora de recogida.
- **PULocationID**: ID de ubicación de recogida.
- **DOLocationID**: ID de ubicación de destino.
- **trip_distance**: Distancia del viaje (en millas).
- **passenger_count**: Número de pasajeros.
- **fare_amount**: Monto de la tarifa básica del viaje.
- **total_amount**: Monto total del viaje.
- **store_and_fwd_flag**: Indicador si los datos del viaje fueron almacenados antes de ser enviados.
- **RatecodeID**: Código de la tarifa aplicada.
- **extra**: Cargos adicionales.
- **mta_tax**: Impuesto de la Autoridad de Transporte Metropolitano.
- **tolls_amount**: Monto de peajes.
- **improvement_surcharge**: Cargos de mejora.

**Utilidad del Dataset**:
- **Análisis de Demanda**: Identificar patrones de demanda y analizar las tendencias de viajes en diferentes zonas y horarios.
- **Optimización de Rutas**: Utilizar datos de ubicaciones de recogida y destino para optimizar rutas y reducir tiempos de viaje.
- **Predicción de Tarifas**: Implementar modelos predictivos para estimar el monto total de los viajes.
- **Evaluación de Eficiencia Operativa**: Analizar la distancia y duración de los viajes para mejorar la eficiencia de la flota.
