# 🚕 Implementación de Vehículos Ambientalmente Amigables en Nueva York

![Descripción de la imagen](img/taxis.jpg)

## 🌍 Descripción General

Este proyecto tiene como finalidad asesorar a una empresa de transporte de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York. Se busca identificar las mejores zonas para iniciar el negocio, considerando la rentabilidad y los patrones de movilidad, alineando así los objetivos financieros con un impacto positivo en el medio ambiente.

## 🎯 Objetivos del Proyecto

 **🔍 Análisis de Patrones de Movilidad y Demanda en Zonas Estratégicas**

**Descripción:**
Este objetivo busca identificar las zonas y horarios de alta demanda para optimizar la operación de la flota. Al entender mejor dónde y cuándo se necesita más transporte, podemos posicionar los taxis de manera eficiente para maximizar la cobertura y reducir los tiempos de espera.

**Indicadores:**

- **Número de Viajes por Zona y Hora:** Mide el número total de viajes iniciados en cada zona y hora del día.
- **Frecuencia de Viajes:** Número de viajes en diferentes franjas horarias (mañana, tarde, noche).
- **Puntos de Recogida y Destino más Comunes:** Identificación de los lugares más frecuentados para inicio y fin de los viajes.

**Métricas:**

- **Viajes por Hora:** Promedio de viajes por hora en diferentes zonas.
- **Tiempo de Espera Medio:** Tiempo promedio que los pasajeros esperan un taxi en las zonas de alta demanda.
- **Saturación de Zonas:** Porcentaje de veces que una zona está en su capacidad máxima de taxis disponibles.

 **📍 Determinación de Zonas Óptimas para Operaciones Sostenibles**

**Descripción:**
Este objetivo se centra en desarrollar un sistema de recomendación que combine rentabilidad y sostenibilidad. Al identificar las zonas más eficientes y ecológicas para operar, podemos reducir las emisiones de CO₂ y mejorar la rentabilidad de la flota.

**Indicadores:**

- **Reducción de Emisiones de CO₂:** Comparación de emisiones antes y después de la optimización de rutas.
- **Costos Operativos por Zona:** Análisis de los costos operativos en diferentes zonas para identificar las más rentables.
- **Eficiencia de Rutas:** Evaluación de la eficiencia de las rutas en términos de distancia y tiempo.

**Métricas:**

- **Emisiones de CO₂ por Viaje:** Cantidad de CO₂ emitido por viaje en diferentes zonas.
- **Costos de Combustible por Zona:** Costos promedio de combustible por zona de operación.
- **Distancia Promedio de Viajes:** Distancia promedio de los viajes en zonas óptimas.

 **📊 Generación de Informes para Decisiones Estratégicas**

**Descripción:**
Crear informes detallados que faciliten una toma de decisiones informada. Estos informes presentarán datos clave y análisis que ayudarán a los stakeholders a entender el desempeño de la flota y a tomar decisiones estratégicas para mejorar la operación y la sostenibilidad.



## 👥 Equipo del Proyecto
- **Vera Guillen** - Analista de Datos
- **Gustavo Coello** - Ingeniero de Datos
- **Camilo Casilimas** - Científico de Datos
- **Alberto Bernal** - Científico de Datos

## 🧠 Sistema de Recomendación

Desarrollaremos un sistema de recomendación basado en datos históricos desde enero de 2023 hasta agosto de 2024. Este sistema recomendará a los conductores de la flota que se desplacen a la zona más cercana con alta demanda histórica, calculada por hora, día de la semana y mes. Utilizaremos una muestra de 50 vehículos para medir los KPI históricamente y tomaremos un periodo de 4 meses para evaluar el modelo predictivo. Esto permitirá optimizar la operación diaria y maximizar la eficiencia de los conductores, asegurando que estén en los lugares correctos en los momentos correctos para satisfacer la demanda de manera efectiva.

## 📈 Indicadores Clave de Rendimiento (KPI)
1. **Número de Viajes por Zona y Hora**  
   - **Descripción**: Mide el número total de viajes iniciados en cada zona y hora del día.  
   - **Meta**: Maximizar la disponibilidad de la flota en zonas y horarios de alta demanda.

2. **Ingresos Totales por Zona**  
   - **Descripción**: Mide el total de ingresos generados en cada zona de recogida.  
   - **Meta**: Identificar y optimizar las zonas más rentables para maximizar los ingresos.

3. **Duración Promedio del Viaje por Zona**  
   - **Descripción**: Mide la duración promedio de los viajes iniciados en cada zona.  
   - **Meta**: Optimizar las rutas para reducir la duración promedio de los viajes.

## 🗓️ Cronograma de Trabajo

### 📝 Fases del Proyecto
| Fase del Proyecto             | Actividades Principales                                   | Responsable       | Duración | Fechas                       |
|--------------------------------|------------------------------------------------------------|-------------------|----------|------------------------------|
| **Fase 1: Recopilación de Datos** | - Identificación de fuentes de datos <br> - Recolección de datasets | Gustavo           | 2 días   | 4 - 5 de Noviembre de 2024   |
| **Fase 2: Preparación de Datos**  | - Limpieza de datos <br> - Selección de características <br> - Integración de datasets | Gustavo           | 4 días   | 6 - 9 de Noviembre de 2024   |
| **Fase 3: Análisis Exploratorio** | - Análisis descriptivo <br> - Visualización inicial de datos | Vera             | 3 días   | 10 - 12 de Noviembre de 2024 |
| **Fase 4: Modelado Predictivo**   | - Desarrollo de modelos <br> - Validación de modelos    | Camilo            | 5 días   | 13 - 17 de Noviembre de 2024 |
| **Fase 5: Optimización de Rutas** | - Algoritmos de optimización <br> - Evaluación de rutas optimizadas | Camilo y Gustavo | 3 días   | 18 - 20 de Noviembre de 2024 |
| **Fase 6: Generación de Informes** | - Preparación de informes visuales <br> - Presentación de resultados | Vera             | 1 día    | 21 de Noviembre de 2024      |

## 📄 Entregables
- **Informe Final**: Documento detallado con análisis, metodología, hallazgos y recomendaciones.
- **Presentación Ejecutiva**: Diapositivas para stakeholders e inversores, resaltando puntos clave.
- **Pipeline de Datos Documentado**: Infraestructura de datos automatizada con documentación técnica.
- **Modelos Predictivos**: Sistemas implementados para el sistema de recomendación y análisis futuro.

## 🛠️ Herramientas y Tecnologías

- **Análisis de Datos**: Python (Pandas, NumPy), SQL, Jupyter Notebooks.
- **Visualización**: Matplotlib, Seaborn, Tableau.
- **Machine Learning**: Scikit-learn, TensorFlow.
- **Pipeline de Datos**: AWS S3, AWS Lambda, MySQL en AWS RDS.
- **Colaboración y Gestión**: GitHub, Slack, Trello, Microsoft Teams.

## 📢 Comunicación y Reuniones
- **Reuniones Diarias**: Stand-ups cada mañana para seguimiento de avances y obstáculos.
- **Reuniones Semanales**: Revisión de progreso, planificación y resolución de problemas.
- **Actualizaciones al PO**: Informes periódicos y reuniones para mantener alineación con objetivos.

## ⚠️ Riesgos y Mitigación
- **Retrasos en la obtención de datos**: Identificar fuentes alternativas y priorizar datasets críticos.
- **Inconsistencias en datos**: Implementar validaciones rigurosas y limpieza exhaustiva.
- **Cambios en requerimientos**: Mantener comunicación constante con el PO para adaptar el alcance de manera oportuna.

## 📬 Contacto

## 🤝 Cómo Contribuir
Para contribuir al proyecto, sigue estos pasos:

1. Clona el repositorio desde GitHub:
   ```bash
   git clone [URL del repositorio]
   ```

