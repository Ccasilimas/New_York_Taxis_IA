import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Viabilidad para Flota de Taxis Ecológicos en Nueva York",
    page_icon="🚖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Tema personalizado
def load_custom_css():
    st.markdown("""
        <style>
        .main {
            background-color: #f0f2f6; /* Gris Claro */
            color: #333;
        }
        .stHeader, .stSubheader, .stText {
            color: #333;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
            animation: blink 1s step-end infinite;
        }
        .stMarkdown h1 {
            color: #1f77b4; /* Azul */
        }
        .stMarkdown h2 {
            color: #ff7f0e; /* Naranja */
        }
        .stMarkdown h3 {
            color: #2ca02c; /* Verde */
        }
        .stMarkdown p {
            font-size: 16px;
        }
        @keyframes blink {
            50% {
                opacity: 0.5;
            }
        }
        .css-1vkb0c3 {
            background-color: #f0f2f6; /* Gris Claro */
        }
        .css-15nxh3m {
            background-color: #f0f2f6; /* Gris Claro */
        }
        </style>
        """, unsafe_allow_html=True)

load_custom_css()

# Título
st.title("🚖 Análisis de Viabilidad para Flota de Taxis Ecológicos en Nueva York")

# Introducción
with st.expander("🌍 Introducción"):
    st.write("""
    Este proyecto tiene como objetivo asesorar a una empresa de transporte de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York...
    """)

# Análisis de Viabilidad
with st.expander("💡 Análisis de Viabilidad"):
    st.write("""
    **Objetivo del Análisis:** Evaluar la viabilidad de implementar una flota de taxis ecológicos en Nueva York, considerando aspectos económicos, ambientales y operativos.
    """)

# Datos y Metodología
with st.expander("📊 Datos y Metodología"):
    st.write("""
    **Fuentes de Datos:** Se utilizaron datos históricos de movilidad urbana, emisiones de CO2, y costos operativos.
    
    **Metodología:** El análisis se llevó a cabo mediante modelado predictivo y simulaciones para identificar las áreas de mayor demanda y los beneficios ambientales potenciales.
    """)

# Resultados del Análisis
with st.expander("📈 Resultados del Análisis"):
    st.write("""
    **Rentabilidad:** Las simulaciones indican una mejora significativa en la rentabilidad debido a la reducción de costos operativos y el aumento de la demanda por taxis ecológicos.

    **Impacto Ambiental:** Se estima una reducción del 20% en las emisiones de CO2 con la implementación de la flota propuesta.
    """)

# Recomendaciones
with st.expander("📝 Recomendaciones"):
    st.write("""
    1. **Implementar Flotas Piloto:** Iniciar con una flota piloto de 50 vehículos en las áreas de mayor demanda identificadas.
    2. **Evaluación Continua:** Monitorear y evaluar continuamente el desempeño de la flota para ajustar las estrategias operativas y de expansión.
    3. **Incentivos y Subvenciones:** Buscar incentivos y subvenciones gubernamentales para apoyar la transición hacia una flota ecológica.
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

# Cronograma de Trabajo
st.header("🗓️ Cronograma de Trabajo")
data_timeline = {
    "Fase": ["Recopilación de Datos", "Preparación de Datos", "Análisis Exploratorio", "Modelado Predictivo", "Optimización de Rutas", "Generación de Informes"],
    "Duración": ["2 días", "4 días", "3 días", "5 días", "3 días", "1 día"],
    "Fechas": ["4-5 Nov 2024", "6-9 Nov 2024", "10-12 Nov 2024", "13-17 Nov 2024", "18-20 Nov 2024", "21 Nov 2024"]
}
df_timeline = pd.DataFrame(data_timeline)
st.dataframe(df_timeline.style.set_properties(**{
    'background-color': '#f0f2f6',
    'color': '#333',
    'border-color': '#fff'
}))

# Herramientas y Tecnologías
st.header("🛠️ Herramientas y Tecnologías")
data_herramientas = {
    "Categoría": ["Análisis de Datos", "Visualización", "Machine Learning", "Pipeline de Datos", "Colaboración y Gestión"],
    "Herramientas": ["Python (Pandas, NumPy), SQL, Jupyter Notebooks", "Matplotlib, Seaborn, Tableau", "Scikit-learn, TensorFlow", "AWS S3, AWS Lambda, MySQL en AWS RDS", "GitHub, Slack, Trello, Microsoft Teams"]
}
df_herramientas = pd.DataFrame(data_herramientas)
st.dataframe(df_herramientas.style.set_properties(**{
    'background-color': '#f0f2f6',
    'color': '#333',
    'border-color': '#fff'
}))

# Riesgos y Mitigación
st.header("⚠️ Riesgos y Mitigación")
data_riesgos = {
    "Riesgo": ["Retrasos en datos", "Inconsistencias", "Cambios en requerimientos"],
    "Estrategia de Mitigación": ["Identificar fuentes alternativas", "Implementar validaciones rigurosas", "Mantener comunicación con PO"]
}
df_riesgos = pd.DataFrame(data_riesgos)
st.dataframe(df_riesgos.style.set_properties(**{
    'background-color': '#f0f2f6',
    'color': '#333',
    'border-color': '#fff'
}))

# Contacto
st.header("📬 Contacto")
st.write("""
- Vera Guillen - [LinkedIn](https://www.linkedin.com/in/vera-guillen-9b464a303/)
- Gustavo Coello - [LinkedIn](https://www.linkedin.com/in/gustavo-coello-01039b270/)
- Alberto Bernal - [LinkedIn](https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/)
- Camilo Casilimas - [LinkedIn](https://www.linkedin.com/in/camilo-casilimas/)
""")

# Cómo Contribuir
st.header("🤝 Cómo Contribuir")
st.write("Clona el repositorio y comienza a contribuir.")
