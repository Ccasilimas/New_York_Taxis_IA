# 🌟 **Ciclo de Vida del Dato**

## 1️⃣ Ingesta de Datos
**Descripción**: Recopilación y almacenamiento inicial de datos desde diversas fuentes.

**Tecnologías y Herramientas**:
- **AWS S3**: Almacenamiento de datasets originales en formato .parquet o .csv.
- **Python**: Scripts de descarga y carga de datos.

**Pasos Involucrados**:
- **Descarga de Datos**: Obtención de datasets de fuentes públicas o privadas.
- **Almacenamiento Inicial**: Guardar archivos de datos en un bucket de S3.

## 2️⃣ Procesamiento y ETL
**Descripción**: Transformación y limpieza de datos para prepararlos para el análisis.

**Tecnologías y Herramientas**:
- **Python y pandas**: Transformación y limpieza de datos.
- **SQLAlchemy**: Interacción con la base de datos MySQL.
- **AWS Lambda y EC2**: Ejecución automática y escalable de scripts de ETL.

**Pasos Involucrados**:
- **Extracción**: Lectura de archivos desde S3.
- **Transformación**: Limpieza y estructuración de datos con pandas.
- **Carga**: Inserción de datos procesados en la base de datos MySQL en AWS RDS.

## 3️⃣ Almacenamiento
**Descripción**: Gestión y almacenamiento de datos transformados en una base de datos relacional.

**Tecnologías y Herramientas**:
- **MySQL en AWS RDS**: Almacenamiento de datos estructurados.

**Pasos Involucrados**:
- **Creación de Tablas**: Definición de la estructura de las tablas.
- **Carga de Datos**: Inserción de datos en las tablas.
- **Indexación**: Creación de índices para optimizar las consultas.

## 4️⃣ Análisis
**Descripción**: Realización de EDA y cálculos de KPIs.

**Tecnologías y Herramientas**:
- **Python y pandas**: Análisis exploratorio y cálculo de KPIs.
- **SQLAlchemy**: Consultas a la base de datos.

**Pasos Involucrados**:
- **EDA**: Análisis para entender la estructura y calidad de los datos.
- **Cálculo de KPIs**: Definición y cálculo de KPIs (Número de Viajes, Ingresos Totales, Duración Promedio).

## 5️⃣ Visualización
**Descripción**: Presentación de datos y KPIs en visualizaciones comprensibles.

**Tecnologías y Herramientas**:
- **Amazon QuickSight**: Creación de dashboards interactivos.

**Pasos Involucrados**:
- **Desarrollo de Dashboards**: Diseño e implementación de visualizaciones.
- **Publicación**: Acceso a dashboards para stakeholders.

## 6️⃣ Automatización y Monitoreo
**Descripción**: Automatización y monitoreo de procesos ETL para asegurar eficiencia y corrección.

**Tecnologías y Herramientas**:
- **AWS Step Functions**: Orquestación de flujos de trabajo.
- **AWS CloudWatch**: Monitorización y registro de ejecuciones.

**Pasos Involucrados**:
- **Automatización del ETL**: Orquestación de procesos ETL con Step Functions.
- **Monitorización**: Configuración de CloudWatch para monitorear y capturar logs de ejecución.

## 7️⃣ Seguridad y Compliance 🔐
**Descripción**: Asegurar el manejo seguro y conforme a normativas de los datos.

**Tecnologías y Herramientas**:
- **AWS IAM**: Gestión de roles y permisos.
- **AWS KMS**: Cifrado de datos en reposo y en tránsito.

**Pasos Involucrados**:
- **Configuración de Permisos