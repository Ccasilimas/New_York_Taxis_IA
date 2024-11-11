# Descripción y Utilidad de los Datasets del Proyecto

![Descripción de la imagen](/img/cargaelectrica.jpg)

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

## 4. Dataset de Emisiones de CO₂
**Descripción del Contenido**: Este dataset contiene información sobre las emisiones de CO₂ en diferentes áreas de Nueva York. Los datos incluyen el nombre del lugar, el periodo de tiempo y el valor de las emisiones medido en toneladas métricas.

**Columnas Incluidas**:
- **geo_place_name**: Nombre del lugar donde se midieron las emisiones.
- **time_period**: Periodo de tiempo durante el cual se midieron las emisiones.
- **data_value**: Valor de las emisiones de CO₂ en toneladas métricas.

**Utilidad del Dataset**:
- **Análisis de Impacto Ambiental**: Evaluar las áreas con mayores emisiones y comparar con las zonas de operación de los taxis eléctricos.
- **Reducción de Emisiones**: Medir el impacto de la implementación de taxis eléctricos en la reducción de emisiones de CO₂.
- **Planificación de Rutas**: Identificar rutas con menores emisiones y optimizar la operación de la flota para reducir el impacto ambiental.

## 5. Dataset de Tráfico
**Descripción del Contenido**: Este dataset contiene información sobre los volúmenes de tráfico en diferentes segmentos viales de Nueva York. Incluye datos por distrito, año, mes, día, hora y el volumen de tráfico medido en número de vehículos.

**Columnas Incluidas**:
- **boro**: Distrito administrativo.
- **yr**: Año del conteo.
- **m**: Mes del conteo.
- **d**: Día del conteo.
- **HH**: Hora del día.
- **vol**: Volumen de tráfico (número de vehículos).
- **SegmentId**: ID del segmento vial.

**Utilidad del Dataset**:
- **Optimización de Rutas**: Utilizar los datos de tráfico para planificar rutas más eficientes y reducir tiempos de viaje.
- **Análisis de Congestión**: Identificar áreas y momentos del día con mayor congestión para evitar demoras.
- **Planificación Estratégica**: Mejorar la operación de la flota al considerar el tráfico en la planificación de rutas.

## 6. Dataset de Especificaciones de Vehículos de Gasolina
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

## 7. Dataset de Vehículos de Combustible Alternativo en EE.UU.
**Descripción del Contenido**: Este dataset contiene información sobre vehículos que utilizan combustibles alternativos en los Estados Unidos. Incluye datos como la categoría del vehículo, el modelo, el año del modelo, el fabricante, el tipo de combustible y la eficiencia de combustible combinada.

**Columnas Incluidas**:
- **Category**: Categoría del vehículo.
- **Model**: Modelo del vehículo.
- **Model Year**: Año del modelo.
- **Manufacturer**: Fabricante del vehículo.
- **Fuel**: Tipo de combustible (por ejemplo, etanol, gas natural).
- **Alternative Fuel Economy Combined**: Eficiencia de combustible combinada para combustibles alternativos.
- **Conventional Fuel Economy Combined**: Eficiencia de combustible combinada para combustibles convencionales.
- **Transmission Type**: Tipo de transmisión.
- **Drivetrain**: Tipo de tracción.

**Utilidad del Dataset**:
- **Comparación de Eficiencia**: Comparar la eficiencia de vehículos con combustibles alternativos frente a vehículos convencionales.
- **Reducción de Emisiones**: Evaluar el potencial de los combustibles alternativos para reducir las emisiones de CO₂.
- **Decisiones de Flota**: Informar decisiones sobre la incorporación de vehículos de combustibles alternativos en la flota.

## 8. Dataset de Vehículos Eléctricos
**Descripción del Contenido**: Este dataset contiene información detallada sobre vehículos eléctricos. Incluye datos sobre la marca, el modelo, la autonomía en kilómetros, la eficiencia energética, la capacidad de carga rápida y el precio en euros.

**Columnas Incluidas**:
- **Brand**: Marca del vehículo.
- **Model**: Modelo del vehículo.
- **Range_Km**: Autonomía en kilómetros.
- **Efficiency_WhKm**: Eficiencia energética en Wh por kilómetro.
- **FastCharge_KmH**: Kilómetros de carga rápida por hora.
- **RapidCharge**: Indicador de capacidad de carga rápida.
- **PriceEuro**: Precio en euros.

**Utilidad del Dataset**:
- **Análisis de Eficiencia**: Evaluar la eficiencia energética de los vehículos eléctricos en comparación con vehículos de combustión interna.
- **Planificación de Flota**: Determinar qué modelos de vehículos eléctricos son más adecuados para la flota en términos de autonomía y eficiencia.
- **Reducción de Costos**: Analizar el potencial de reducción de costos operativos mediante la adopción de vehículos eléctricos.

## 9. Dataset de For Hire Vehicles (FHV) Activos

**Descripción del Contenido**
Este dataset contiene información sobre los vehículos for hire (FHV) activos en Nueva York, autorizados por la Taxi and Limousine Commission (TLC). Incluye detalles sobre el estado del permiso, el número de licencia del vehículo, el tipo de vehículo, y datos del propietario y la base.

**Columnas Incluidas**:
- **Active**: Indica si el permiso está activo (`YES`) o no (`NO`).
- **Vehicle License Number**: Número de licencia del vehículo FHV.
- **License Type**: Tipo de licencia TLC (FOR HIRE VEHICLE).
- **Vehicle VIN Number**: Número de Identificación del Vehículo (VIN).
- **Wheelchair Accessible**: Indicador de accesibilidad para sillas de ruedas (`WAV` o vacío).
- **Vehicle Year**: Año del vehículo.
- **Base Type**: Tipo de base (`LIVERY`, `LUXURY`, `COMMUNITY CAR`, `VAN`, `PARATRANSIT`).
- **VEH**: Indicador de vehículo híbrido (`HYB`).
- **Last Date Updated**: Última fecha de actualización.
- **Last Time Updated**: Última hora de actualización.

**Columnas Irrelevantes para el Proyecto**
- **Name**: Nombre del propietario.
- **Expiration Date**: Fecha de vencimiento del permiso.
- **Permit License Number**: Número de permiso.
- **DMV License Plate Number**: Número de placa DMV.
- **Certification Date**: Fecha de certificación.
- **Hack Up Date**: Fecha de puesta en servicio.
- **Base Number**: Número de la base.
- **Base Name**: Nombre de la base.
- **Base Telephone Number**: Número de teléfono de la base.
- **Website**: Página web de la base.
- **Base Address**: Dirección de la base.
- **Reason**: Código de razón (`G` si activo, `A`, `B`, `C` o combinación si no activo).
- **Order Date**: Fecha de orden de suspensión.

**Utilidad del Dataset**:
- **Análisis Comparativo**: Permite comparar la eficiencia operativa y las emisiones entre diferentes tipos de vehículos, incluyendo taxis y FHVs.
- **Evaluación de Sostenibilidad**: Ayuda a analizar la proporción de vehículos híbridos (`HYB`) y accesibles para sillas de ruedas (`WAV`), crucial para iniciativas de sostenibilidad y accesibilidad.
- **Estado de Permisos**: Utiliza la información sobre el estado del permiso (`Active`) para identificar y anali

## Dataset de Zonas de Taxis

**Descripción del Contenido**
Este dataset contiene información sobre las zonas de taxis en Nueva York, proporcionado por la **Taxi and Limousine Commission (TLC)**. Las zonas están definidas por ubicaciones específicas y se utilizan para analizar y gestionar los patrones de viajes de taxis y FHV en la ciudad.

**Columnas Incluidas:**
- **LocationID**: Identificador único de la ubicación.
- **Borough**: Nombre del distrito al que pertenece la ubicación (por ejemplo, Manhattan, Queens, Bronx).
- **Zone**: Nombre de la zona específica dentro del distrito.
- **service_zone**: Zona de servicio (puede especificar si es para taxis amarillos, verdes u otros servicios).

**Utilidad del Dataset:**
- **Análisis de Patrones de Viaje**: Permite analizar los patrones de recogida y destino en función de las zonas.
- **Gestión de Demandas**: Ayuda a identificar zonas con alta demanda y optimizar la asignación de recursos.
- **Planificación de Rutas**: Facilita la planificación estratégica para la optimización de rutas de taxis y FHV.

