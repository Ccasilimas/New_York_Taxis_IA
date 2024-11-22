
# 🚕 Implementación de Vehículos Ambientalmente Amigables en Nueva York

![nyctaxis](https://github.com/user-attachments/assets/b064bc10-83dd-423d-a89f-1b74a894b2f2)

## 🌍 Descripción General

Este proyecto tiene como finalidad asesorar a una empresa de transporte de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York. Se busca identificar las mejores zonas para iniciar el negocio, considerando la rentabilidad y los patrones de movilidad, alineando así los objetivos financieros con un impacto positivo en el medio ambiente.

## 🎯 Objetivos del Proyecto

1. **Análisis de Patrones de Movilidad y Demanda en Zonas Estratégicas** 🔍  
   * Identificar zonas y horarios de alta demanda.  
   * Optimizar la operación de la flota.

2. **Determinación de Zonas Óptimas para Operaciones Sostenibles** 📍  
   * Desarrollar un sistema de recomendación.  
   * Combinar rentabilidad y sostenibilidad.

3. **Generación de Informes para Decisiones Estratégicas** 📊  
   * Crear informes detallados.  
   * Facilitar toma de decisiones informada.

## 👥 Equipo del Proyecto

| Nombre          | Cargo              |
|------------------|--------------------|
| Vera Guillen     | Analista de Datos |
| Gustavo Coello   | Ingeniero de Datos |
| Alberto Bernal   | Científico de Datos |
| Camilo Casilimas | Ingeniero de Datos |

## 🧠 Sistema de Recomendación

Desarrollamos un sistema de recomendación basado en un modelo de regresión lineal que utiliza datos históricos desde enero de 2023 hasta agosto de 2024. Este sistema incluirá:

* Predicciones de demanda considerando zonas adyacentes.
* Análisis de datos históricos por:
  * Hora.
  * Día de la semana.
  * Mes.
* Recomendaciones detalladas de las zonas con mayor demanda predicha.
* Comparación detallada entre las mejores zonas basadas en la demanda predicha y la zona actual del conductor.


## 📈 Indicadores Clave de Rendimiento (KPI)

### 1. Número de Viajes por Zona y Hora
* **Descripción**: Mide el número total de viajes iniciados en cada zona y hora del día.  
* **Meta**: Maximizar la disponibilidad de la flota en zonas y horarios de alta demanda.

### 2. Ingresos Totales por Zona
* **Descripción**: Mide el total de ingresos generados en cada zona de recogida.  
* **Meta**: Identificar y optimizar las zonas más rentables para maximizar los ingresos.

### 3. Duración Promedio del Viaje por Zona
* **Descripción**: Mide la duración promedio de los viajes iniciados en cada zona.  
* **Meta**: Optimizar las rutas para reducir la duración promedio de los viajes.

## 🗓️ Cronograma de Trabajo

### Fases del Proyecto

| Fase                  | Actividades                                   | Responsable | Duración | Fechas       |
|-----------------------|-----------------------------------------------|-------------|----------|--------------|
| **Fase 1:** Recopilación de Datos | • Identificación de fuentes<br>• Recolección de datasets | Gustavo     | 2 días   | 4-5 Nov 2024 |
| **Fase 2:** Preparación de Datos  | • Limpieza<br>• Selección de características<br>• Integración | Alberto     | 4 días   | 6-9 Nov 2024 |
| **Fase 3:** Análisis Exploratorio | • Análisis descriptivo<br>• Visualización inicial | Alberto        | 3 días   | 10-12 Nov 2024 |
| **Fase 4:** Modelado Predictivo   | • Desarrollo de modelos<br>• Validación | Camilo       | 5 días   | 13-17 Nov 2024 |
| **Fase 5:** Optimización de Rutas | • Algoritmos<br>• Evaluación | Gustavo     | 3 días   | 18-20 Nov 2024 |
| **Fase 6:** Generación de Informes| • Informes visuales<br>• Presentación | Vera        | 1 día    | 21 Nov 2024  |

## 📄 Entregables

* **Informe Final**  
  * Análisis detallado.  
  * Metodología.  
  * Hallazgos.  
  * Recomendaciones.

* **Presentación Ejecutiva**  
   * Puntos clave del proyecto.

* **Pipeline de Datos**  
  * Infraestructura automatizada.  
  
* **Modelos Predictivos**  
  * Sistema de recomendación.  
  

## 🛠️ Herramientas y Tecnologías

| Categoría             | Herramientas                                  |
|-----------------------|-----------------------------------------------|
| **Análisis de Datos** | • Python (Pandas, NumPy)• SQL • Jupyter Notebooks |
| **Visualización**     | • Matplotlib • Seaborn • PowerBI       |
| **Machine Learning**  | • Scikit-learn •                |
| **Pipeline de Datos** | • AWS S3 • AWS Lambda • MySQL en AWS RDS |
| **Colaboración y Gestión** | • GitHub • Slack • Trello • Microsoft Teams |

## 📢 Comunicación y Reuniones

### Reuniones Periódicas
* **Diarias**: Stand-ups matutinos.  
* **Semanales**: Revisión de progreso.  
* **Con PO**: Actualizaciones periódicas.

## ⚠️ Riesgos y Mitigación

| Riesgo              | Estrategia de Mitigación              |
|---------------------|---------------------------------------|
| Retrasos en datos   | Identificar fuentes alternativas.     |
| Inconsistencias     | Implementar validaciones rigurosas.   |
| Cambios en requerimientos | Mantener comunicación con PO.   |

## 📬 Contacto

* **Vera Guillen** - Analista de Datos.  [LinkedIn](https://www.linkedin.com/in/vera-guillen-9b464a303/)
* **Gustavo Coello** - Ingeniero de Datos [LinkedIn](https://www.linkedin.com/in/gustavo-coello-01039b270/).  
* **Alberto Bernal** - Cientifico de Datos [LinkedIn](https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/).  
* **Camilo Casilimas** - Arquitecto e Ingeniero de Datos  [LinkedIn](https://www.linkedin.com/in/camilo-casilimas/).

## 🤝 Cómo Contribuir

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Ccasilimas/New_York_Taxis_IA
