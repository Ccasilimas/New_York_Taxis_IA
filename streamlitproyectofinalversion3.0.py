import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title="Taxis Ambientalmente Amigables en Nueva York",
    page_icon="🚖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS para colores personalizados y animaciones
st.markdown("""
    <style>
    body {
        background-color: #F0F2F6;
        color: #333;
    }
    .dark-mode body {
        background-color: #333;
        color: #F0F2F6;
    }
    .main {
        padding: 2rem;
    }
    h1, h2, h3 {
        transition: color 1s ease-in-out;
    }
    h1 {
        color: #1f77b4;
        animation: flicker 3s infinite;
    }
    h2 {
        color: #ff7f0e;
    }
    h3 {
        color: #2ca02c;
    }
    @keyframes flicker {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .icon {
        margin-right: 10px;
    }
    .table {
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 1rem;
    }
    .table th, .table td {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
    }
    .table th {
        background-color: #f2f2f2;
    }
    .dark-mode .table th {
        background-color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# Tema Oscuro/Claro
dark_mode = st.sidebar.checkbox("🌗 Activar Modo Oscuro")
if dark_mode:
    st.markdown('<div class="dark-mode"></div>', unsafe_allow_html=True)

# Título
st.title("🚖 Implementación de Vehículos Ambientalmente Amigables en Nueva York")

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
    "Cargo": ["Analista de Datos", "Ingeniero de Datos", "Científico de Datos", "Científico de Datos"],
    "LinkedIn": [
        "https://www.linkedin.com/in/vera-guillen-9b464a303/",
        "https://www.linkedin.com/in/gustavo-coello-01039b270/",
        "https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/",
        "https://www.linkedin.com/in/camilo-casilimas/"
    ]
}
df_equipo = pd.DataFrame(data_equipo)
for i, row in df_equipo.iterrows():
    st.markdown(f"**{row['Nombre']}** - {row['Cargo']} - [LinkedIn]({row['LinkedIn']})")

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
st.dataframe(df_timeline.style.set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#9DA9A0'), ('color', 'black')]},
    {'selector': 'td', 'props': [('background-color', '#C0CAAD'), ('color', 'black')]}
]))

# Herramientas y Tecnologías
st.header("🛠️ Herramientas y Tecnologías")
data_herramientas = {
    "Categoría": ["Análisis de Datos", "Visualización", "Machine Learning", "Pipeline de Datos", "Colaboración y Gestión"],
    "Herramientas": ["Python (Pandas, NumPy), SQL, Jupyter Notebooks", "Matplotlib, Seaborn, Tableau", "Scikit-learn, TensorFlow", "AWS S3, AWS Lambda, MySQL en AWS RDS", "GitHub, Slack, Trello, Microsoft Teams"]
}
df_herramientas = pd.DataFrame(data_herramientas)
st.dataframe(df_herramientas.style.set