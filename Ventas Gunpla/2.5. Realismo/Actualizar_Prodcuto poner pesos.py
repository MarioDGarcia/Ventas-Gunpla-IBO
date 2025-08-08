import pandas as pd

# Cargar datos
df_prod = pd.read_csv("IBO_Gunplas.csv")

# Asignar peso base = 1
df_prod['peso'] = 1.0

# Peso máximo: Barbatos Lupus Rex
mask_lupusrex = df_prod['nombreProducto'].str.contains("Lupus Rex", case=False)
df_prod.loc[mask_lupusrex, 'peso'] = 50

# Segundo más alto: Barbatos Lupus (pero no Lupus Rex)
mask_lupus = df_prod['nombreProducto'].str.contains("Barbatos Lupus", case=False) & ~mask_lupusrex
df_prod.loc[mask_lupus, 'peso'] = 40

# Luego: Otros Barbatos (pero no Lupus ni Lupus Rex)
mask_barb_otros = df_prod['nombreProducto'].str.contains("Barbatos", case=False) & ~mask_lupus & ~mask_lupusrex
df_prod.loc[mask_barb_otros, 'peso'] = 30

# Normalizar pesos para que sumen 1
df_prod['peso'] /= df_prod['peso'].sum()

# Guardar resultado
df_prod.to_csv("productos_pesados.csv", index=False)
print("Pesos ajustados. Barbatos y sus variantes tienen mayor prioridad.")
