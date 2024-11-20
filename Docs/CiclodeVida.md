# 🚖 Ciclo de Vida del Dato en el Proyecto de Predicción de Demanda de Taxis FHV en NYC

## 📌 Introducción
El objetivo de este proyecto es desarrollar un modelo predictivo que ayude a los conductores de taxis FHV (For-Hire Vehicle) en la ciudad de Nueva York a identificar las mejores zonas a las que desplazarse, optimizando sus oportunidades de recoger pasajeros. Utilizamos datos históricos de viajes, información de tráfico y detalles geográficos para cumplir con este propósito. A continuación, se detalla el ciclo de vida del dato desde su origen hasta su uso en el modelo predictivo.

---

## 1️⃣ Origen y Recolección de Datos

### 1.1 🛺 Datos de Taxis FHV (`taxi_fhv_data`)
- **Fuente:** Registros históricos proporcionados por empresas de transporte y agencias regulatorias.
- **Contenido:**
  - `id`
  - `Pickup_datetime`
  - `DropOff_datetime`
  - `PULocationID`
  - `DOLocationID`
  - `source` (origen del dato)

### 1.2 🚦 Datos de Tráfico (`trafico`)
- **Fuente:** Sensores y sistemas de monitoreo de tráfico en NYC.
- **Contenido:**
  - `id`
  - `Yr` (Año)
  - `M` (Mes)
  - `D` (Día)
  - `HH` (Hora)
  - `MM` (Minuto)
  - `Vol` (Volumen de tráfico)
  - `SegmentID`
  - `Direction`

### 1.3 🗺️ Datos de Zonas de Taxis (`taxi_zones`)
- **Fuente:** Administración de Transporte de NYC.
- **Contenido:**
  - `LocationID`
  - `Borough`
  - `Zone`
  - `service_zone`

---

## 2️⃣ Almacenamiento
- **Base de Datos:** MySQL  
- **Esquema:** `UrbanTransit`  
- **Tablas Principales:**
  - `taxi_fhv_data`
  - `trafico`
  - `taxi_zones`

---

## 3️⃣ Procesamiento y Transformación (ETL)

### 3.1 🔍 Extracción
- **Herramientas Utilizadas:**
  - Python  
  - Librerías: `pandas`, `sqlalchemy`, `mysql-connector-python`, `python-dotenv`
- **Scripts:**
  - `nyc_taxi_etl.py`: Extrae datos desde la base de datos.

### 3.2 🔄 Transformación
- **Unión de Datos:**
  - **Datos de Taxis y Tráfico:** Se unen basándose en componentes temporales: `Pickup_datetime` con `Yr`, `M`, `D`, `HH`, `MM`.  
    - Nueva columna: `traffic_volume` (promedio del volumen de tráfico).
  - **Mapeo de Zonas:** `PULocationID` se mapea a `pickup_borough` utilizando `taxi_zones`.

- **Creación de Variables Temporales:**
  - A partir de `Pickup_datetime` se extraen:
    - `pickup_year`, `pickup_month`, `pickup_day`, `pickup_hour`, `pickup_minute`
    - `day_of_week` (0=Lunes, 6=Domingo)

- **Depuración de Datos:**
  - Eliminación de columnas no esenciales:
    - `temperature`, `trip_miles`, `driver_pay`, `VendorID`, `trip_time`.

### 3.3 💾 Carga
- **Tabla de Destino:** `enriched_taxi_data`
- **Proceso:**
  - Los datos transformados se cargan en la tabla enriquecida para su posterior análisis.

---

## 4️⃣ Análisis y Modelado

### 4.1 📊 Preparación de Datos
- **Selección de Variables para el Modelo:**
  - **Variables de Entrada (X):**
    - `day_of_week`
    - `pickup_hour`
    - `pickup_borough` (One-Hot Encoding)
    - `traffic_volume`
  - **Variable Objetivo (y):**
    - `trip_count` (número de viajes en un período y zona específicos)

- **Agrupación de Datos:**
  - Los datos se agrupan por `pickup_borough`, `day_of_week` y `pickup_hour` para calcular `trip_count`.

- **Codificación de Variables Categóricas:**
  - Se aplica **One-Hot Encoding** a `pickup_borough`.

### 4.2 🤖 Entrenamiento del Modelo
- **Algoritmo Utilizado:** Regresión Lineal
- **Proceso:**
  - División del dataset en conjuntos de entrenamiento y prueba.
  - Entrenamiento del modelo con los datos de entrenamiento.
  - Evaluación del modelo con métricas como **MAE** y **R²**.

- **Variables Finales Utilizadas:**
  - `day_of_week`, `pickup_hour`, `pickup_borough` (codificada), `traffic_volume`

---

## 5️⃣ Despliegue
- **Implementación del Modelo:**
  - El modelo entrenado se integra en una aplicación o sistema que proporciona predicciones en tiempo real.
- **Funcionalidad:**
  - Los conductores ingresan la hora actual y reciben recomendaciones sobre las mejores zonas para dirigirse.

---

