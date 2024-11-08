# README - Columnas No Utilizadas en los Datasets del Proyecto

## Dataset de Medallions
### Columnas No Utilizadas:
- **Vehicle VIN Number**
  - **Razón**: No es necesario para los análisis de emisiones, costos operativos o predicciones de tarifas.
- **Last Date Updated**
  - **Razón**: Esta columna solo indica la última fecha de actualización y no aporta valor al análisis de datos históricos o predictivos.
- **Last Time Updated**
  - **Razón**: Similar a la columna anterior, esta columna no es relevante para nuestros objetivos de análisis.

## Dataset de Taxis Amarillos y Verdes
### Columnas No Utilizadas:
- **store_and_fwd_flag**
  - **Razón**: Esta columna indica si los datos del viaje fueron almacenados antes de ser enviados, lo cual no es relevante para el análisis de emisiones o eficiencia.
- **RatecodeID**
  - **Razón**: Aunque describe el tipo de tarifa, no es fundamental para nuestros análisis de emisiones y eficiencia operativa.
- **extra**
  - **Razón**: Representa cargos adicionales, que no son críticos para el análisis de rendimiento del vehículo y rutas.
- **mta_tax**
  - **Razón**: Impuesto de la Autoridad de Transporte Metropolitano, no relevante para análisis operativos.
- **tolls_amount**
  - **Razón**: Monto de peajes, que no es necesario para el análisis de rutas y emisiones.
- **improvement_surcharge**
  - **Razón**: Cargos de mejora, no pertinentes para el análisis de eficiencia y sostenibilidad.

## Dataset de For-Hire Vehicles (FHV) Activos
### Columnas No Utilizadas:
- **Base Name**
  - **Razón**: El nombre de la base del vehículo no es relevante para el análisis de rendimiento operativo o de emisiones.
- **Wheelchair Accessible**
  - **Razón**: Aunque importante para la accesibilidad, esta columna no afecta directamente los análisis de eficiencia de combustible y emisiones de CO₂.
- **Base Number**
  - **Razón**: Similar a Base Name, no tiene relevancia directa para los análisis operativos y ambientales.

## Dataset de Tráfico
### Columnas No Utilizadas:
- **boro**
  - **Razón**: Aunque útil para segmentar datos por distrito, no es crítico para los análisis de optimización de rutas y emisiones.
- **yr**
  - **Razón**: La columna año puede ser redundante si ya estamos analizando por meses y días específicos.
- **HH**
  - **Razón**: La hora específica puede no ser necesaria para todos los análisis, dependiendo del enfoque en tendencias diarias completas.

## Dataset de Emisiones de CO₂
### Columnas No Utilizadas:
- **geo_place_name**
  - **Razón**: La granularidad de ubicación por nombre puede no ser esencial si ya estamos segmentando por áreas más grandes o tiempo.
- **measurement_method**
  - **Razón**: El método de medición puede no ser relevante si solo estamos interesados en los valores de emisión.

## Dataset de Especificaciones de Vehículos
### Columnas No Utilizadas:
- **Manufacturer**
  - **Razón**: La marca del fabricante no es crucial para el análisis de eficiencia operativa y emisiones.
- **Model**
  - **Razón**: El modelo específico no es necesario si ya estamos segmentando por tipo y año del vehículo.

## Dataset de Vehículos de Combustible Alternativo en EE.UU.
### Columnas No Utilizadas:
- **Category**
  - **Razón**: La categoría del vehículo puede no ser relevante si ya estamos segmentando por tipo de combustible y año del modelo.
- **Transmission Type**
  - **Razón**: El tipo de transmisión no afecta directamente las emisiones y eficiencia del combustible en el contexto de nuestro análisis.

## Dataset de Vehículos Eléctricos
### Columnas No Utilizadas:
- **PriceEuro**
  - **Razón**: El precio en euros no es relevante para nuestros análisis en Nueva York y el rendimiento operativo del vehículo.
- **RapidCharge**
