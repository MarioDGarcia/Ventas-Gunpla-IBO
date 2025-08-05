import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Cargar archivos
productos = pd.read_csv("IBO_Gunplas.csv")  # usa la columna 'id_nuevo'
paises = pd.read_csv("Paises con continene.csv")  # usa la columna 'id_pais' y 'continente'

# Obtener listas necesarias
lista_productos = productos['id_nuevo'].dropna().unique().tolist()

paises = paises.dropna(subset=["id_pais", "continente"])
lista_paises = paises[['id_pais', 'continente']].copy()  # asegurar que sea copia

# Definir pesos por continente
pesos_continente = {
    "Asia": 0.4,
    "América": 0.25,
    "Europa": 0.2,
    "África": 0.1,
    "Caribe": 0.05
}

# Asignar pesos de forma segura
lista_paises.loc[:, 'peso'] = lista_paises['continente'].map(pesos_continente)
lista_paises = lista_paises.dropna(subset=['peso']).reset_index(drop=True)

# Crear función para generar una fecha aleatoria
def fecha_aleatoria():
    inicio = datetime(2022, 1, 1)
    fin = datetime(2024, 12, 31)
    return inicio + timedelta(days=random.randint(0, (fin - inicio).days))

# Parámetros de simulación
num_ventas = 100_000

# Generar datos simulados
ventas_simuladas = []

for i in range(1, num_ventas + 1):

    fecha = fecha_aleatoria().strftime('%Y-%m-%d')
    id_producto = random.choice(lista_productos)
    pais = lista_paises.sample(weights=lista_paises['peso']).iloc[0]['id_pais']
    # Generar unidades con prioridad en 1-5 y 13-17, pero permitiendo todos los valores de 1-20
    opciones = list(range(1, 21))
    pesos = [0.13]*5 + [0.02]*7 + [0.08]*5 + [0.01]*3  # 1-5: más peso, 6-12: menos, 13-17: medio, 18-20: bajo
    # Ajustar pesos para que sumen 1
    suma_pesos = sum(pesos)
    pesos = [p/suma_pesos for p in pesos]
    unidades = random.choices(opciones, weights=pesos, k=1)[0]
    
    
    ventas_simuladas.append([i, fecha, id_producto, pais, unidades])

# Crear DataFrame
df_ventas = pd.DataFrame(ventas_simuladas, columns=['id_venta', 'fecha_venta', 'id_producto', 'id_pais', 'unidades'])

# Guardar como CSV
df_ventas.to_csv("Ventas_gunplas_simuladas.csv", index=False)
print("Archivo guardado como Ventas_gunplas_simuladas.csv")
