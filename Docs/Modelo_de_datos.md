# 🗂️ Relaciones entre las Columnas  

## 🚖 1. Datos de Viajes (Yellow, Green y FHV) y NYC Taxi Zone Lookup  
*Relación Principal:*  
- 📍 Pickup_LocationID y DropOff_LocationID en los datasets de viajes (*Yellow Trip, **Green Trip* y *FHV) se relacionan con LocationID en el dataset **NYC Taxi Zone Lookup*.  

---

## 🚦 2. Datos de Viajes y Volúmenes de Tráfico  
*Relación Principal:*  
- 🛣️ Pickup_LocationID y DropOff_LocationID en los datasets de viajes se pueden relacionar indirectamente con SegmentID y WktGeom en el dataset *Automated Traffic Volume Counts* para análisis geoespaciales y patrones de tráfico.  
- 🌆 Boro en *Automated Traffic Volume Counts* se puede relacionar con Borough en *NYC Taxi Zone Lookup*.  

---

## 🌡️ 3. Datos de Viajes y Temperaturas Promedio (Mensuales)  
*Relación Principal:*  
- 🕒 Pickup_DateTime y DropOff_DateTime en los datasets de viajes se pueden relacionar con Mes en el dataset de *Temperaturas Promedio* para analizar el impacto de las condiciones meteorológicas en la demanda de taxis.  
- 🗺️ Borough en *NYC Taxi Zone Lookup* se puede utilizar para alinear las temperaturas de cada borough con los datos de viajes.  

---  

🎯 *Nota:* Estas relaciones facilitan análisis integrales entre los datos de viajes, tráfico y condiciones climáticas.