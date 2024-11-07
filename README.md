# Implementación de Vehículos Ambientalmente Amigables en Nueva York

## Descripción del Proyecto
Este proyecto tiene como objetivo evaluar la viabilidad económica y ambiental para implementar una nueva flota de taxis ambientalmente amigables en Nueva York. Se busca identificar las mejores zonas para iniciar operaciones, considerando rentabilidad, demanda y datos ambientales.

## Equipo del Proyecto
- **Vera**: Encargada de visualización de datos.
- **Alberto**: Responsable de análisis de datos.
- **Camilo**: Encargado de modelado predictivo.
- **Gustavo**: Encargado de ingeniería de datos.

## Objetivo General
Asesorar a la empresa en la evaluación de la viabilidad económica y ambiental para implementar una nueva flota de taxis ambientalmente amigables en Nueva York.

## Objetivos Específicos
### Análisis de Patrones de Movilidad y Demanda
- Utilizar datos de movilidad para identificar zonas y horarios de alta demanda.
- Optimizar la operación de la flota en áreas con mayor oportunidad de ingresos.

### Evaluación de Emisiones de CO₂ y Optimización de Rutas
- Analizar las emisiones en diversas rutas y horarios.
- Identificar rutas que reduzcan consumo de combustible y emisiones.

### Determinación de Zonas Óptimas para Operaciones Sostenibles
- Desarrollar un sistema de recomendación que combine rentabilidad y reducción de emisiones.
- Priorizar zonas donde el impacto ambiental positivo se alinee con objetivos financieros.

### Generación de Informes para Decisiones Estratégicas
- Crear informes detallados y visuales para inversores y directivos.
- Facilitar una toma de decisiones informada sobre la implementación de la flota.

## Datasets Utilizados
1. **Dataset de Taxis Amarillos y Verdes**
   - **Columnas a Mantener**: `pickup_datetime`, `PULocationID`, `DOLocationID`, `trip_distance`, `passenger_count`, `fare_amount`, `total_amount`
   - **Columnas a Borrar**: `VendorID`, `RatecodeID`, `store_and_fwd_flag`, `payment_type`, `extra`, `mta_tax`, `tip_amount`, `tolls_amount`, `improvement_surcharge`, `congestion_surcharge`

2. **Dataset de For-Hire Vehicles (FHV) Activos**
   - **Columnas a Mantener**: `Active`, `Vehicle License Number`, `Vehicle Year`, `Base Name`, `Wheelchair Accessible`
   - **Columnas a Borrar**: `Name`, `License Type`, `Expiration Date`, `Permit License Number`, `DMV License Plate Number`, `Certification Date`, `Hack Up Date`, `Base Number`, `Base Type`, `VEH`, `Base Telephone Number`, `Website`, `Base Address`, `Reason`, `Order Date`, `Last Date Updated`, `Last Time Updated`

3. **Dataset de Medallions**
   - **Columnas a Mantener**: `License Number`, `Vehicle VIN Number`, `Vehicle Type`, `Model Year`, `Agent Name`, `Expiration Date`
   - **Columnas a Borrar**: `Name`, `Current Status`, `DMV License Plate Number`, `Medallion Type`, `Agent Telephone Number`, `Agent Website Address`, `Agent Address`, `Last Date Updated`, `Last Time Updated`

4. **Dataset de Tráfico**
   - **Columnas a Mantener**: `boro`, `yr`, `m`, `d`, `HH`, `vol`, `SegmentId`
   - **Columnas a Borrar**: `RequestID`, `mm`, `WktGeom`, `street`, `fromSt`, `toSt`, `Direction`

5. **Dataset de Emisiones de CO₂**
   - **Columnas a Mantener**: `geo_place_name`, `time_period`, `data_value`
   - **Columnas a Borrar**: `unique_id`, `indicator_id`, `name`, `measure`, `measure_info`, `geo_type_name`, `geo_join_id`, `start_date`, `message`

6. **Dataset de Especificaciones de Vehículos**
   - **Columnas a Mantener**: `Year`, `Manufacturer`, `Model`, `fuelType`, `comb08`, `co2`
   - **Columnas a Borrar**: `barrels08`, `city08`, `highway08`, `fuelCost08`, `ghgScore`, `cylinders`, `displ`, `drive`, `trany`, `VClass`, `atvType`

7. **Dataset de Vehículos de Combustible Alternativo en EE.UU.**
   - **Columnas a Mantener**: `Category`, `Model`, `Model Year`, `Manufacturer`, `Fuel`, `Alternative Fuel Economy Combined`, `Conventional Fuel Economy Combined`, `Transmission Type`, `Drivetrain`
   - **Columnas a Borrar**: `All-Electric Range`, `PHEV Total Range`, `Alternative Fuel Economy City`, `Alternative Fuel Economy Highway`, `Conventional Fuel Economy City`, `Conventional Fuel Economy Highway`, `Engine Type`, `Engine Size`, `Engine Cylinder Count`, `Number of Passengers`, `Heavy-Duty Power System`, `Notes`

8. **Dataset de Vehículos Eléctricos**
   - **Columnas a Mantener**: `Brand`, `Model`, `Range_Km`, `Efficiency_WhKm`, `FastCharge_KmH`, `RapidCharge`, `PriceEuro`
   - **Columnas a Borrar**: `AccelSec`, `TopSpeed_KmH`, `PowerTrain`, `PlugType`, `BodyStyle`, `Segment`, `Seats`

## Avances del Día
1. **Incorporación de Nuevos Datasets**
   - Añadido el Dataset de Vehículos de Combustible Alternativo en EE.UU. y el Dataset de Vehículos Eléctricos.
   - Identificación y selección de columnas clave para el análisis.

2. **Análisis de los Nuevos Datasets**
   - Evaluación de la utilidad de los nuevos datasets para los objetivos específicos del proyecto.

3. **Integración en el Proyecto**
   - Planificación y actualización del plan de trabajo para integrar los nuevos datasets en el análisis existente.

4. **Preparación para el Análisis Exploratorio de Datos (EDA)**
   - Organización y preprocesamiento de los nuevos datasets para el EDA.

5. **Revisión de Progreso**
   - Resumen de los avances y establecimiento de próximas tareas y prioridades.

## Próximos Pasos
- **Análisis Exploratorio de Datos (EDA)**: Iniciar el EDA para descubrir patrones y relaciones en los datos.
- **Modelado y Predicción**: Desarrollar modelos predictivos para optimizar rutas y reducir emisiones.
- **Generación de Informes**: Preparar informes visuales y detallados con los resultados del análisis y presentarlos a los stakeholders.

## Conclusión
Hoy hemos avanzado significativamente en la ampliación de nuestra base de datos y la preparación para un análisis más profundo. La incorporación de nuevos datasets nos proporciona una base sólida para tomar decisiones informadas sobre la implementación de vehículos sostenibles en nuestra flota, alineándonos perfectamente con los objetivos del proyecto y las expectativas del cliente.

## Contacto del Equipo
- **Vera**: Encargada de visualización de datos.
- **Alberto**: Responsable de análisis de datos.
- **Camilo**: Encargado de modelado predictivo.
- **Gustavo**: Encargado de ingeniería de datos.

# Plan del Proyecto: Implementación de Vehículos Ambientalmente Amigables en Nueva York

## Fases del Proyecto

| Fase del Proyecto           | Actividades Principales                                                         | Responsable         | Duración   | Fechas                          |
|-----------------------------|----------------------------------------------------------------------------------|---------------------|------------|----------------------------------|
| **Fase 1: Recopilación de Datos**  | - Identificación de fuentes de datos <br> - Recolección de datasets              | Gustavo             | 2 semanas  | 1 - 14 de Noviembre de 2024     |
| **Fase 2: Preparación de Datos**   | - Limpieza de datos <br> - Selección de características <br> - Integración de datasets | Gustavo             | 3 semanas  | 15 de Nov - 5 de Dic de 2024    |
| **Fase 3: Análisis Exploratorio**  | - Análisis descriptivo <br> - Visualización inicial de datos                     | Vera                | 2 semanas  | 6 - 19 de Diciembre de 2024     |
| **Fase 4: Modelado Predictivo**    | - Desarrollo de modelos <br> - Validación de modelos                            | Camilo              | 4 semanas  | 20 de Dic - 16 de Ene de 2025   |
| **Fase 5: Optimización de Rutas**  | - Algoritmos de optimización <br> - Evaluación de rutas optimizadas              | Camilo y Gustavo    | 3 semanas  | 17 de Ene - 6 de Feb de 2025    |
| **Fase 6: Evaluación Ambiental**   | - Análisis de emisiones <br> - Evaluación de impacto ambiental                   | Alberto             | 2 semanas  | 7 - 20 de Febrero de 2025       |
| **Fase 7: Generación de Informes** | - Preparación de informes visuales <br> - Presentación de resultados             | Vera                | 3 semanas  | 21 de Feb - 13 de Mar de 2025   |
| **Fase 8: Implementación Piloto**  | - Implementación de fase piloto <br> - Monitoreo y recopilación de datos         | Todo el equipo      | 4 semanas  | 14 de Mar - 10 de Abr de 2025   |
| **Fase 9: Ajustes y Mejoras**      | - Análisis de datos del piloto <br> - Ajustes en modelos y estrategias           | Todo el equipo      | 2 semanas  | 11 - 24 de Abril de 2025        |
| **Fase 10: Expansión Gradual**     | - Expansión de la flota <br> - Continuación de monitoreo y optimización continua | Todo el equipo      | 4 semanas  | 25 de Abr - 22 de May de 2025   |
