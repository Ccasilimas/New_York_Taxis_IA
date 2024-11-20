import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Taxis Ambientalmente Amigables en Nueva York",
    page_icon="🚖",
    layout="wide"
)

# Título principal
st.title("Implementación de Vehículos Ambientalmente Amigables en Nueva York")

# Descripción general
st.header("🌍 Descripción General")
st.write("""
Este proyecto tiene como finalidad asesorar a una empresa de transporte de pasajeros en la evaluación y viabilidad de implementar una nueva flota de taxis ambientalmente amigables en la ciudad de Nueva York.
El análisis incluye patrones de movilidad, zonas estratégicas y oportunidades para operar de manera sostenible, contribuyendo al desarrollo urbano y la reducción de emisiones de carbono.
""")

# Objetivos del Proyecto
st.header("🎯 Objetivos del Proyecto")
st.markdown("""
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
st.dataframe(df_equipo.style.set_properties(**{
    'background-color': '#f7f7f7',
    'color': '#333',
    'border': '1px solid #ddd'
}))

# Sistema de Recomendación
st.header("🧠 Sistema de Recomendación")
st.write("""
Utilizando análisis avanzado de datos y herramientas de machine learning, se desarrolla un sistema que identifica las áreas más eficientes para operar taxis eléctricos, considerando factores como:
- Demanda de pasajeros.
- Cercanía a estaciones de carga.
- Emisiones estimadas de CO2.
""")

# Visualización: Demanda de Pasajeros
st.header("📊 Visualización: Demanda de Pasajeros")
# Datos simulados para la visualización
data = {
    "Zona": ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"],
    "Demanda": [35000, 20000, 15000, 10000, 5000]
}
df_demanda = pd.DataFrame(data)
fig, ax = plt.subplots()
sns.barplot(data=df_demanda, x="Zona", y="Demanda", palette="coolwarm", ax=ax)
ax.set_title("Demanda de Pasajeros por Zona")
ax.set_xlabel("Zona")
ax.set_ylabel("Demanda (número de viajes)")
st.pyplot(fig)

# Visualización: Horarios de Alta Demanda
st.header("⏰ Horarios de Alta Demanda")
# Datos simulados para la visualización
horarios = {
    "Hora": [f"{i}:00" for i in range(24)],
    "Viajes": [400, 300, 200, 150, 100, 120, 800, 1500, 2500, 3000, 3500, 4000,
               4200, 4300, 4500, 4200, 4000, 3800, 3000, 2500, 2000, 1500, 800, 500]
}
df_horarios = pd.DataFrame(horarios)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_horarios, x="Hora", y="Viajes", marker="o", color="blue", ax=ax)
ax.set_title("Horarios de Alta Demanda")
ax.set_xlabel("Hora")
ax.set_ylabel("Número de Viajes")
st.pyplot(fig)

# Estaciones de Carga: Visualización Mapa
st.header("📍 Estaciones de Carga Eléctrica")
st.write("Aquí se muestra un ejemplo de ubicaciones estratégicas de estaciones de carga eléctrica para apoyar la operación de taxis ambientalmente amigables.")
# Datos simulados para mapa
map_data = pd.DataFrame({
    'lat': [40.7128, 40.73061, 40.758896, 40.807537, 40.748817],
    'lon': [-74.0060, -73.935242, -73.985130, -73.962572, -73.985428],
    'Estación': ['Station 1', 'Station 2', 'Station 3', 'Station 4', 'Station 5']
})
st.map(map_data)

# Conclusiones
st.header("📌 Conclusiones")
st.write("""
Este proyecto representa una oportunidad para transformar la movilidad urbana en Nueva York, implementando tecnologías más limpias y sostenibles.
Con el análisis presentado, se espera optimizar las operaciones y mejorar la calidad del aire en la ciudad.
""")

# Fin del Proyecto
st.success("¡Gracias por explorar el proyecto!")
