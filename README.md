# 🚕 Environmentally Friendly Vehicle Implementation in New York

![nyctaxis](https://github.com/user-attachments/assets/b064bc10-83dd-423d-a89f-1b74a894b2f2)

## Overview 🌍

This project aims to advise a passenger transport company in evaluating the feasibility of implementing a new environmentally friendly taxi fleet in New York City. We seek to identify the best areas to start operations, considering profitability and mobility patterns, thus aligning financial objectives with a positive environmental impact.

## Table of Contents
- [Project Objectives](#project-objectives)
- [Team Members](#team-members)
- [Recommendation System](#recommendation-system)
- [Key Performance Indicators](#key-performance-indicators)
- [Deliverables](#deliverables)
- [Tools & Technologies](#tools--technologies)
- [Communication](#communication)
- [Risk Management](#risk-management)
- [Contact Information](#contact-information)
- [How to Contribute](#how-to-contribute)

## Project Objectives 🎯

1. **Analysis of Mobility Patterns and Demand in Strategic Areas**
   * Identify high-demand zones and peak hours
   * Optimize fleet operations

2. **Determination of Optimal Zones for Sustainable Operations**
   * Develop a recommendation system
   * Balance profitability with sustainability

3. **Generation of Strategic Decision Reports**
   * Create detailed analysis reports
   * Facilitate informed decision-making

## Team Members 👥

| Name             | Position          |
|------------------|-------------------|
| Vera Guillen     | Data Analyst      |
| Gustavo Coello   | Data Engineer     |
| Alberto Bernal   | Data Scientist    |
| Camilo Casilimas | Data Engineer     |

## Recommendation System 🧠

Our recommendation system is based on a linear regression model using historical data from January 2023 to August 2024. The system includes:

* Demand predictions considering adjacent zones
* Historical data analysis by:
  * Hour
  * Day of the week
  * Month
* Detailed recommendations for highest predicted demand zones
* Comparative analysis between best zones based on predicted demand and driver's current zone

## Key Performance Indicators 📈

### 1. Trips per Zone and Hour
* **Description**: Measures total trips initiated in each zone and hour
* **Goal**: Maximize fleet availability in high-demand areas and times

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

## Communication 📢

### Regular Meetings
* **Daily**: Morning stand-ups
* **Weekly**: Progress reviews
* **Product Owner**: Regular updates

## Risk Management ⚠️

| Risk | Mitigation Strategy |
|------|-------------------|
| Data Delays | Identify alternative sources |
| Data Inconsistencies | Implement rigorous validation |
| Requirement Changes | Maintain regular PO communication |

## Contact Information 📬

* **Vera Guillen** - Data Analyst - [LinkedIn](https://www.linkedin.com/in/vera-guillen-9b464a303/)
* **Gustavo Coello** - Data Engineer - [LinkedIn](https://www.linkedin.com/in/gustavo-coello-01039b270/)
* **Alberto Bernal** - Data Scientist - [LinkedIn](https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/)
* **Camilo Casilimas** - Data Architect & Engineer - [LinkedIn](https://www.linkedin.com/in/camilo-casilimas/)

## How to Contribute 🤝

1. Clone the repository:
```bash
git clone https://github.com/Ccasilimas/New_York_Taxis_IA
```