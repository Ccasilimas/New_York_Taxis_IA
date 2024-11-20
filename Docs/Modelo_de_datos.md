# 📋 Detalle de Tablas y Relaciones

## 🛺 Tabla: `taxi_fhv_data`
**Descripción:** Contiene registros detallados de los viajes de taxis FHV en NYC.

### Columnas:
- **`id`**: Identificador único del registro (clave primaria).
- **`Pickup_datetime`**: Fecha y hora de recogida del pasajero.
- **`DropOff_datetime`**: Fecha y hora de llegada al destino.
- **`PULocationID`**: ID de la ubicación de recogida.
- **`DOLocationID`**: ID de la ubicación de destino.
- **`source`**: Fuente de los datos (por ejemplo, 'yellow', 'green', 'FHV').

### Relaciones:
- **`PULocationID`** y **`DOLocationID`** se relacionan con **`LocationID`** en la tabla `taxi_zones` para obtener información geográfica y administrativa de las zonas.

---

## 🚦 Tabla: `trafico`
**Descripción:** Proporciona información sobre el volumen de tráfico en diferentes segmentos y momentos en NYC.

### Columnas:
- **`id`**: Identificador único del registro.
- **`Yr`**: Año del registro.
- **`M`**: Mes del registro.
- **`D`**: Día del registro.
- **`HH`**: Hora del registro.
- **`MM`**: Minuto del registro.
- **`Vol`**: Volumen de tráfico.
- **`SegmentID`**: Identificador del segmento de tráfico.
- **`Direction`**: Dirección del tráfico.

### Relaciones:
- Se relaciona temporalmente con **`Pickup_datetime`** de `taxi_fhv_data` y `enriched_taxi_data` a través de **`Yr`**, **`M`**, **`D`**, **`HH`**, **`MM`**, para enriquecer los datos de taxis con información de tráfico.

---

## 🌡️ Tabla: `temperaturas`
**Descripción:** Contiene las temperaturas promedio mensuales de cada borough de NYC.

### Columnas:
- **`id`**: Identificador único del registro.
- **`Mes`**: Mes del año.
- **`Manhattan`**: Temperatura promedio en Manhattan.
- **`Brooklyn`**: Temperatura promedio en Brooklyn.
- **`Queens`**: Temperatura promedio en Queens.
- **`The_Bronx`**: Temperatura promedio en The Bronx.
- **`Staten_Island`**: Temperatura promedio en Staten Island.

### Relaciones:
- Se relaciona con **`pickup_month`** en `enriched_taxi_data` para enriquecer los datos de taxis con información de temperatura.

---

## 🗺️ Tabla: `taxi_zones`
**Descripción:** Proporciona información geográfica y administrativa de las zonas de taxis en NYC.

### Columnas:
- **`LocationID`**: Identificador único de la zona (clave primaria).
- **`Borough`**: Borough al que pertenece la zona.
- **`Zone`**: Nombre de la zona.
- **`service_zone`**: Zona de servicio.

### Relaciones:
- **`LocationID`** se relaciona con **`PULocationID`** y **`DOLocationID`** en `taxi_fhv_data` y `enriched_taxi_data` para obtener detalles de ubicación.

---

## 📊 Tabla: `enriched_taxi_data`
**Descripción:** Contiene los datos de taxis enriquecidos con información de tráfico y temperatura.

### Columnas:
- **`id`**: Identificador único del registro (clave primaria).
- **`Pickup_datetime`**: Fecha y hora de recogida del pasajero.
- **`DropOff_datetime`**: Fecha y hora de llegada al destino.
- **`PULocationID`**: ID de la ubicación de recogida.
- **`DOLocationID`**: ID de la ubicación de destino.
- **`pickup_borough`**: Borough de recogida.
- **`traffic_volume`**: Volumen de tráfico en el momento y lugar de recogida.
- **`source`**: Fuente de los datos.
- **`pickup_year`**: Año de la recogida.
- **`pickup_month`**: Mes de la recogida.
- **`pickup_day`**: Día de la recogida.
- **`pickup_hour`**: Hora de la recogida.
- **`pickup_minute`**: Minuto de la recogida.

### Relaciones:
- **Con `taxi_fhv_data`**: Este conjunto de datos es una versión enriquecida de `taxi_fhv_data`.
- **Con `trafico`**: Relacionado a través de componentes temporales (**`Yr`**, **`M`**, **`D`**, **`HH`**, **`MM`**) para incorporar el volumen de tráfico.
- **Con `temperaturas`**: Mediante **`pickup_month`** y **`pickup_borough`** para añadir información de temperatura (aunque se eliminó la columna `temperature` en actualizaciones recientes).
- **Con `taxi_zones`**: A través de **`PULocationID`** para obtener detalles sobre la zona de recogida.

---

## 🔗 Resumen de Relaciones
- **`taxi_fhv_data`** se relaciona con `taxi_zones` mediante **`PULocationID`** y **`DOLocationID`**.
- **`trafico`** se relaciona con `enriched_taxi_data` mediante componentes temporales para añadir información de tráfico.
- **`temperaturas`** se relaciona con `enriched_taxi_data` a través de **`pickup_month`** y **`pickup_borough`** (aunque actualmente la columna `temperature` ha sido eliminada del modelo predictivo).
- **`enriched_taxi_data`** centraliza la información de las otras tablas para proporcionar un conjunto de datos completo para el análisis y modelado.
