@ -1 +1,101 @@
# Proyecto_final_Henry
# Implementación de Vehículos Ambientalmente Amigables en Nueva York

## Descripción General
Este proyecto tiene como finalidad asesorar a una empresa de transporte de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York. Se busca identificar las mejores zonas para iniciar el negocio, considerando la rentabilidad, los patrones de movilidad y los datos ambientales, alineando así los objetivos financieros con un impacto positivo en el medio ambiente.

## Objetivos del Proyecto
- **Análisis de Patrones de Movilidad y Demanda en Zonas Estratégicas**: Identificar zonas y horarios de alta demanda para optimizar la operación de la flota.
- **Evaluación de Emisiones de CO₂ y Optimización de Rutas**: Analizar rutas que contribuyan a la reducción de consumo de combustible y emisiones.
- **Determinación de Zonas Óptimas para Operaciones Sostenibles**: Desarrollar un sistema de recomendación que combine rentabilidad y sostenibilidad.
- **Generación de Informes para Decisiones Estratégicas**: Crear informes detallados que faciliten una toma de decisiones informada.

## Equipo del Proyecto
- **Analistas de Datos**: 2 profesionales encargados del análisis de movilidad y emisiones.
- **Ingeniero de Datos**: Responsable de construir y mantener el pipeline de datos.
- **Data Scientist**: Encargado de desarrollar modelos predictivos y sistemas de recomendación.

## Cronograma de Trabajo
### Semana 1: Investigación y Recopilación de Datos
| Día       | Actividad                                                                              | Responsable           |
|-----------|----------------------------------------------------------------------------------------|------------------------|
| Lunes     | Reunión de lanzamiento, definición de objetivos y alcance                              | Todo el equipo        |
| Martes    | Recolección de datos de movilidad de taxis en NYC: Utilizar fuentes como NYC TLC       | Analista de Datos 1   |
| Miércoles | Recolección de datos ambientales: Emisiones de CO₂, calidad del aire, contaminación sonora | Analista de Datos 2   |
| Jueves    | Investigación de infraestructura: Disponibilidad y ubicación de estaciones de carga    | Ingeniero de Datos    |
| Viernes   | Análisis Exploratorio de Datos (EDA): Limpieza y preparación de datos, visualizaciones iniciales | Todo el equipo |
| Sábado    | Documentación de hallazgos preliminares: Preparación de resumen para el Product Owner (PO) | Todo el equipo |
| Domingo   | Descanso: Revisión individual de avances y planificación personal                      | -                      |

### Semana 2: Análisis y Evaluación de Datos
| Día       | Actividad                                                                  | Responsable         |
|-----------|----------------------------------------------------------------------------|----------------------|
| Lunes     | Presentación al PO: Exposición de avances, retroalimentación y alineación de objetivos | Todo el equipo      |
| Martes    | Análisis de movilidad: Identificación de zonas y horarios de alta demanda  | Analista de Datos 1 |
| Miércoles | Evaluación de emisiones: Análisis de rutas para reducción de CO₂ y consumo de combustible | Analista de Datos 2 |
| Jueves    | Desarrollo del pipeline de datos: Implementación de procesos ETL, aseguramiento de calidad de datos | Ingeniero de Datos |
| Viernes   | Desarrollo del sistema de recomendación: Aplicación de técnicas de Machine Learning | Data Scientist |
| Sábado    | Validación y ajuste de modelos: Pruebas y optimizaciones necesarias        | Data Scientist      |
| Domingo   | Documentación: Registro detallado de metodologías y resultados             | Todo el equipo      |

### Semana 3: Consolidación y Presentación Final
| Día       | Actividad                                                                | Responsable          |
|-----------|--------------------------------------------------------------------------|-----------------------|
| Lunes     | Integración de resultados: Consolidación de análisis y modelos desarrollados | Analistas y Data Scientist |
| Martes    | Optimización del pipeline de datos: Mejoras en eficiencia y escalabilidad | Ingeniero de Datos   |
| Miércoles | Preparación de informes: Redacción del informe final con hallazgos clave y recomendaciones estratégicas | Todo el equipo |
| Jueves    | Diseño de presentación: Creación de una presentación atractiva y efectiva para stakeholders | Todo el equipo |
| Viernes   | Ensayo de presentación: Práctica y refinamiento de la exposición         | Todo el equipo       |
| Sábado    | Presentación final: Exposición a inversores y directivos, con espacio para preguntas y retroalimentación | Todo el equipo |
| Domingo   | Planificación de pasos siguientes: Ajustes basados en feedback y definición de etapas futuras | Todo el equipo |

## Entregables
- **Informe Final**: Documento detallado con análisis, metodología, hallazgos y recomendaciones.
- **Presentación Ejecutiva**: Diapositivas para stakeholders e inversores, resaltando puntos clave.
- **Pipeline de Datos Documentado**: Infraestructura de datos automatizada con documentación técnica.
- **Modelos Predictivos**: Sistemas implementados para el sistema de recomendación y análisis futuro.

## Herramientas y Tecnologías
- **Análisis de Datos**: Python (Pandas, NumPy), SQL, Jupyter Notebooks.
- **Visualización**: Matplotlib, Seaborn, Tableau.
- **Machine Learning**: Scikit-learn, TensorFlow.
- **Pipeline de Datos**: Apache Airflow, Herramientas ETL.
- **Colaboración y Gestión**: GitHub, Slack, Trello, Microsoft Teams.

## Comunicación y Reuniones
- **Reuniones Diarias**: Stand-ups cada mañana para seguimiento de avances y obstáculos.
- **Reuniones Semanales**: Revisión de progreso, planificación y resolución de problemas.
- **Actualizaciones al PO**: Informes periódicos y reuniones para mantener alineación con objetivos.

## Riesgos y Mitigación
- **Retrasos en la obtención de datos**: Identificar fuentes alternativas y priorizar datasets críticos.
- **Inconsistencias en datos**: Implementar validaciones rigurosas y limpieza exhaustiva.
- **Cambios en requerimientos**: Mantener comunicación constante con el PO para adaptar el alcance de manera oportuna.

## Contacto
- **Product Owner (PO)**: [Nombre del PO] - [Correo electrónico]
- **Equipo Técnico**:
  - Analista de Datos 1: [Nombre] - [Contacto]
  - Analista de Datos 2: [Nombre] - [Contacto]
  - Ingeniero de Datos: [Nombre] - [Contacto]
  - Data Scientist: [Nombre] - [Contacto]

## Cómo Contribuir
Para contribuir al proyecto, sigue estos pasos:

1. Clona el repositorio desde GitHub:
    ```bash
    git clone [URL del repositorio]
    ```
2. Crea una nueva rama para tu tarea:
    ```bash
    git checkout -b nombre-de-tu-rama
    ```
3. Realiza tus cambios y haz commits con mensajes claros:
    ```bash
    git add .
    git commit -m "Descripción de tus cambios"
    ```
4. Envía un pull request describiendo los cambios realizados y su propósito.

## Licencia
Este proyecto se encuentra bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

# Calendario del Proyecto: Implementación de Vehículos Ambientalmente Amigables en Nueva York

## Fases del Proyecto

| Fase del Proyecto           | Actividades Principales                                                         | Responsable         | Duración   | Fechas                          |
|-----------------------------|----------------------------------------------------------------------------------|---------------------|------------|----------------------------------|
| **Fase 1: Recopilación de Datos**  | - Identificación de fuentes de datos <br> - Recolección de datasets              | Gustavo             | 2 días     | 4 - 5 de Noviembre de 2024      |
| **Fase 2: Preparación de Datos**   | - Limpieza de datos <br> - Selección de características <br> - Integración de datasets | Gustavo             | 4 días     | 6 - 9 de Noviembre de 2024      |
| **Fase 3: Análisis Exploratorio**  | - Análisis descriptivo <br> - Visualización inicial de datos                     | Vera                | 3 días     | 10 - 12 de Noviembre de 2024    |
| **Fase 4: Modelado Predictivo**    | - Desarrollo de modelos <br> - Validación de modelos                            | Camilo              | 5 días     | 13 - 17 de Noviembre de 2024    |
| **Fase 5: Optimización de Rutas**  | - Algoritmos de optimización <br> - Evaluación de rutas optimizadas              | Camilo y Gustavo    | 3 días     | 18 - 20 de Noviembre de 2024    |
| **Fase 6: Evaluación Ambiental**   | - Análisis de emisiones <br> - Evaluación de impacto ambiental                   | Alberto             | 1 día      | 21 de Noviembre de 2024         |
| **Fase 7: Generación de Informes** | - Preparación de informes visuales <br> - Presentación de resultados             | Vera                | 1 día      | 22 de Noviembre de 2024         |
