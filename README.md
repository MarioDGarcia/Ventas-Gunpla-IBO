# Generador de Datos Simulados de Ventas de Gunpla (IBO)

Este repositorio contiene un algoritmo en **Python** que genera un conjunto de **100,000 ventas simuladas** de modelos **Gunpla** basados en el universo de **Mobile Suit Gundam: Iron-Blooded Orphans**, correspondientes a los años **2022, 2023 y 2024**.

Estas ventas ficticias incluyen información como:

- **Fecha de la venta**  
- **ID del producto**  
- **País de venta** (con pesos asignados por continente)  
- **Cantidad de unidades vendidas**

El objetivo de este proyecto es crear un conjunto de datos útil para **pruebas de análisis, limpieza y visualización de datos** en escenarios realistas pero controlados.

---

##  Datos “ensuciados” para pruebas de calidad

Además, se incluye un segundo script que **ensucia los datos** de forma intencional, introduciendo errores comunes para simular un entorno realista y poner a prueba técnicas de limpieza. Los errores incluyen:

- **Valores nulos** en diferentes columnas  
- **Fechas mal formateadas** o con texto irreconocible  
- **IDs inválidos** de producto o país  
- **Unidades como texto** (por ejemplo: `"muchas"` o `"??"`)  
- **Duplicación de registros**

---

Este entorno simulado permite practicar conceptos clave de **ciencia de datos**, como:

- Validación y limpieza de datos  
- Manejo de errores y outliers  
- Preparación de datos para visualización o modelos analíticos

---

 Archivos generados:
- `Ventas_gunplas_simuladas.csv`: datos limpios simulados  
- `Ventas_gunplas_sucias.csv`: versión con errores intencionales  

REVISAR ARCHIVO "Limpieza Datos", PARA SEGUIR CON ORDEN

