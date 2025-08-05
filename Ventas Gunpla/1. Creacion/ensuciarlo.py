


import pandas as pd
import numpy as np
import random

# Cargar el archivo limpio
df = pd.read_csv("Ventas_gunplas_simuladas.csv")

# Introducir valores nulos aleatorios
for col in ["id_venta", "Fecha_venta", "id_producto", "Id_Pais", "unidades"]:
    idx = df.sample(frac=0.01).index  # 1% de nulos por columna
    df.loc[idx, col] = np.nan

# Modificar fechas a un formato malo o texto
malas_fechas = df.sample(frac=0.005).index
df.loc[malas_fechas, "Fecha_venta"] = "fecha desconocida"

# Introducir IDs inválidos
df.loc[df.sample(frac=0.005).index, "id_producto"] = 99999  # ID que no existe
df.loc[df.sample(frac=0.005).index, "Id_Pais"] = -1  # ID de país inválido

# Unidades como texto
df.loc[df.sample(frac=0.005).index, "unidades"] = "muchas"
df.loc[df.sample(frac=0.005).index, "unidades"] = "??"

# Duplicar algunas filas
df = pd.concat([df, df.sample(frac=0.01)], ignore_index=True)

# Guardar archivo sucio
df.to_csv("Ventas_gunplas_sucias.csv", index=False)
print("Archivo sucio generado.")
