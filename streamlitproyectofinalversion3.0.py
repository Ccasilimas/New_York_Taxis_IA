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
    Green Route Solutions presenta un estudio de viabilidad para una flota de taxis ecológicos en Nueva York.
    """)

# Quiénes Somos
with st.expander("🌟 Quiénes Somos"):
    st.write("""
    Green Route Solutions es una consultora especializada en soluciones sostenibles para el transporte urbano.

    **Áreas de Especialización:**
    - Análisis de Datos: Optimización de rutas y reducción de la huella de carbono.
    - Análisis de Rutas: Identificación de zonas óptimas para operaciones.
    - Soluciones Sostenibles: Implementación de tecnologías ecológicas.
    """)

# Nuestro Equipo
st.header("👥 Nuestro Equipo")
data_equipo = {
    "Nombre": ["Camilo Casilimas", "Gustavo Coello", "Alberto Bernal", "Vera Guillen"],
    "Cargo": ["Arquitecto e Ingeniero de Datos", "Ingeniero de Datos", "Científico de Datos", "Data Analyst"],
    "LinkedIn": [
        "https://www.linkedin.com/in/camilo-casilimas/",
        "https://www.linkedin.com/in/gustavo-coello-01039b270/",
        "https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/",
        "https://www.linkedin.com/in/vera-guillen-9b464a303/"
    ]
}
df_equipo = pd.DataFrame(data_equipo)
for i, row in df_equipo.iterrows():
    st.markdown(f"**{row['Nombre']}** - {row['Cargo']} - [LinkedIn]({row['LinkedIn']})")

# Objetivo General
with st.expander("🎯 Objetivo General"):
    st.write("""
    Este proyecto tiene como finalidad asesorar a Urban Transit Corp transportadora de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York. Se busca identificar las mejores zonas para iniciar el negocio, considerando la rentabilidad y los patrones de movilidad, alineando así los objetivos financieros con un impacto positivo en el medio ambiente.
    """)

# Objetivos Específicos
with st.expander("📌 Objetivos Específicos"):
    st.write("""
    1. **Análisis de Demanda:** Identificar zonas y horarios de alta demanda para optimizar la operación de la flota.
    2. **Evaluación de Emisiones:** Analizar rutas para reducir el consumo de combustible y emisiones.
    3. **Zonas Óptimas:** Crear un sistema de recomendación que optimice la rentabilidad y reducción de emisiones.
    """)

# Alcance del Proyecto
with st.expander("🔍 ¿Cuál Será El Alcance?"):
    st.write("""
    1. **Recopilación de Datos:** Análisis de datos de demanda de taxis.
    2. **Evaluación de Áreas:** Identificar áreas óptimas para taxis ecológicos.
    3. **Análisis de Costos:** Reducción de costos de operación.
    4. **Estimación de Incentivos:** Evaluación de incentivos fiscales y ambientales.
    """)

# Entregables
with st.expander("📦 ¿Qué Entregaremos?"):
    st.write("""
    1. **Dashboard:** Monitoreo de KPIs: Demanda, Emisiones de CO₂, Rentabilidad.
    2. **Modelo de Machine Learning:** Predicción de demanda y optimización de rutas.
    3. **Análisis Completo:** Evaluación de la viabilidad económica y ambiental de la flota.
    """)

# Metodología
st.header("🔧 Metodología")
st.write("""
Se utilizará el proceso Scrum para la gestión del proyecto.
""")

data_timeline = {
    "Fase del Proyecto": ["Fase 1: Recopilación de Datos", "Fase 2: Preparación de Datos", "Fase 3: Análisis Exploratorio", 
                          "Fase 4: Modelado Predictivo", "Fase 5: Optimización de Rutas", "Fase 6: Evaluación Ambiental", 
                          "Fase 7: Generación de Informes"],
    "Actividades Principales": ["Identificación de fuentes de datos, Recolección de datasets", "Limpieza de datos, Selección de características, Integración de datasets", 
                                "Análisis descriptivo, Visualización inicial de datos", "Desarrollo de modelos, Validación de modelos", 
                                "Algoritmos de optimización, Evaluación de rutas optimizadas", "Análisis de emisiones, Evaluación de impacto ambiental", 
                                "Preparación de informes visuales, Presentación de resultados"],
    "Responsable": ["Gustavo", "Gustavo", "Vera", "Camilo", "Camilo y Gustavo", "Alberto", "Vera"],
    "Duración": ["SPRINT 1", "SPRINT 1", "SPRINT 2", "SPRINT 2", "SPRINT 3", "SPRINT 3", "SPRINT 3"],
    "Fechas": ["5 - 9 de Noviembre de 2024", "10 - 12 de Noviembre de 2024", "13 - 17 de Noviembre de 2024", 
               "18 - 20 de Noviembre de 2024", "21 de Noviembre de 2024", "22 de Noviembre de 2024", "23 de Noviembre de 2024"]
}

df_timeline = pd.DataFrame(data_timeline)
st.dataframe(df_timeline.style.set_properties(**{
    'background-color': '#f0f2f6',
    'color': '#333',
    'border-color': '#fff'
}))

# Tecnologías Clave para el Análisis de Datos
st.header("💻 Tecnologías Clave para el Análisis de Datos")
st.write("""
- Utilizaremos Python como lenguaje principal de programación por su flexibilidad y amplia comunidad de desarrolladores.
- Aprovecharemos los servicios de AWS como Lambda, S3 para procesar y almacenar los datos de manera escalable y eficiente.
- Emplearemos Power BI para generar informes visuales e interactivos que permitan una mejor comprensión de los insights clave.
- Finalmente no utilizaremos Microsoft Azure ni Tableau.
""")

# La Vida del Dato
st.header("🔄 La Vida del Dato")
st.write("""
Desde la recolección hasta el análisis y la visualización, cada dato pasará por un proceso meticuloso que garantiza su calidad y relevancia para la toma de decisiones.
""")

# Contacto
st.header("📬 Contacto")
st.write("""
- Camilo Casilimas - [LinkedIn](https://www.linkedin.com/in/camilo-casilimas/)
- Gustavo Coello - [LinkedIn](https://www.linkedin.com/in/gustavo-coello-01039b270/)
- Alberto Bernal - [LinkedIn](https://www.linkedin.com/in/alberto-bernal-duplat-90a283a2/)
- Vera Guillen - [LinkedIn](https://www.linkedin.com/in/vera-guillen-9b464a303/)
""")

# Cómo Contribuir
st.header("🤝 Cómo Contribuir")
st.write("Clona el repositorio y comienza a contribuir.")
