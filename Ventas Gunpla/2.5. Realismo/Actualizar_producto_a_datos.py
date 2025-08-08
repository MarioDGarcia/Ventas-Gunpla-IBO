import pandas as pd
import numpy as np

# Cargar ventas y productos con pesos
df_ventas = pd.read_csv("Ventas_IBO_Gunpla_V2.0.csv")
df_productos = pd.read_csv("productos_pesados.csv")  # tu archivo con pesos


# Extraer IDs y pesos
productos = df_productos["id_nuevo"].tolist()
pesos = df_productos["peso"].tolist()

# Generar nueva columna de productos según los pesos
df_ventas["id_producto"] = np.random.choice(
    productos,
    size=len(df_ventas),
    p=pesos
)

# Guardar resultado
df_ventas.to_csv("Ventas_IBO_Gunpla_V3.0.csv", index=False)

print("✅ Productos en ventas actualizados según popularidad.")
