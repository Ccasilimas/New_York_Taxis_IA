import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Taxis Ambientalmente Amigables en Nueva York")

# Título
st.title("Implementación de Vehículos Ambientalmente Amigables en Nueva York")

# Descripción general
st.header("🌍 Descripción General")
st.write("""
Este proyecto tiene como finalidad asesorar a una empresa de transporte de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York...
""")

# Objetivos del Proyecto
st.header("🎯 Objetivos del Proyecto")
st.write("""
1. **Análisis de Patrones de Movilidad y Demanda en Zonas Estratégicas**: Identificar zonas y horarios de alta demanda y optimizar la operación de la flota.
2. **Determinación de Zonas Óptimas para Operaciones Sostenibles**: Desarrollar un sistema de recomendación que combine rentabilidad y sostenibilidad.
3. **Generación de Informes para Decisiones Estratégicas**: Crear informes detallados que faciliten la toma de decisiones informada.
""")

# Equipo del Proyecto
st.header("👥 Equipo del Proyecto")
data_equipo = {
    "Nombre": ["Vera Guillen", "Gustavo Coello", "Alberto Bernal", "Camilo Casilimas"],
    "Cargo": ["Analista de Datos", "Ingeniero de Datos", "Científico de Datos", "Científico de Datos"]
}
df_equipo = pd.DataFrame(data_equipo)
st.dataframe(df_equipo)

# Sistema de Recomendación
st.header("🧠 Sistema de Recomendación")
st.write("""
Desarrollaremos un sistema de recomendación basado en datos históricos desde enero de 2023 hasta agosto de 2024. Este sistema incluirá:
- Recomendaciones en tiempo real para conductores.
- Análisis de datos históricos por hora, día de la semana y mes.
- Muestra inicial de 50 vehículos.
- Período de evaluación de 4 meses.
""")

# Indicadores Clave de Rendimiento (KPI)
st.header("📈 Indicadores Clave de Rendimiento (KPI)")
st.write("""
1. **Número de Viajes por Zona y Hora**: Mide el número total de viajes iniciados en cada zona y hora del día.
2. **Ingresos Totales por Zona**: Mide el total de ingresos generados en cada zona de recogida.
3. **Duración Promedio del Viaje por Zona**: Mide la duración promedio de los viajes iniciados en cada zona.
""")

# Cronograma de Trabajo
st.header("🗓️ Cronograma de Trabajo")
data_timeline = {
    "Fase": ["Recopilación de Datos", "Preparación de Datos", "Análisis Exploratorio", "Modelado Predictivo", "Optimización de Rutas", "Generación de Informes"],
    "Duración": ["2 días", "4 días", "3 días", "5 días", "3 días", "1 día"],
    "Fechas": ["4-5 Nov 2024", "6-9 Nov 2024", "10-12 Nov 2024", "13-17 Nov 2024", "18-20 Nov 2024", "21 Nov 2024"]
}
df_timeline = pd.DataFrame(data_timeline)
st.dataframe(df_timeline)

# Herramientas y Tecnologías
st.header("🛠️ Herramientas y Tecnologías")
data_herramientas = {
    "Categoría": ["Análisis de Datos", "Visualización", "Machine Learning", "Pipeline de Datos", "Colaboración y Gestión"],
    "Herramientas": ["Python (Pandas, NumPy), SQL, Jupyter Notebooks", "Matplotlib, Seaborn, Tableau", "Scikit-learn, TensorFlow", "AWS S3, AWS Lambda, MySQL en AWS RDS", "GitHub, Slack, Trello, Microsoft Teams"]
}
df_herramientas = pd.DataFrame(data_herramientas)
st.dataframe(df_herramientas)

# Riesgos y Mitigación
st.header("⚠️ Riesgos y Mitigación")
data_riesgos = {
    "Riesgo": ["Retrasos en datos", "Inconsistencias", "Cambios en requerimientos"],
    "Estrategia de Mitigación": ["Identificar fuentes alternativas", "Implementar validaciones rigurosas", "Mantener comunicación con PO"]
}
df_riesgos = pd.DataFrame(data_riesgos)
st.dataframe(df_riesgos)

# Contacto
st.header("📬 Contacto")
st.write("""
- Vera Guillen - Analista de Datos.
- Gustavo Coello - LinkedIn.
- Alberto Bernal - LinkedIn.
- Camilo Casilimas - LinkedIn.
""")

# Cómo Contribuir
st.header("🤝 Cómo Contribuir")
st.write("""
Clona el repositorio:
""")
