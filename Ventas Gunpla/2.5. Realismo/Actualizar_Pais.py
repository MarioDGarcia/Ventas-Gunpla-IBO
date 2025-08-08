import pandas as pd

# Cargar datos
df_limpio = pd.read_csv("Ventas_IBO_Gunpla_V2.0.csv")
paises = pd.read_csv("Paises con continene.csv").dropna(subset=["id_pais", "continente"])
lista = paises[['id_pais', 'continente']].copy()

# Distribución de pesos por continente
pesos_continente = {
    "Asia": 0.65,        # Fuerte pero no dominante absoluto
    "América": 0.25,     # Incluye EE.UU., LatAm
    "Oceanía": 0.25,     # MISMO nivel que América
    "Europa": 0.08,
    "África": 0.01,
    "Caribe": 0.01
}
lista['peso'] = lista['continente'].map(pesos_continente)

# Reforzar Japón, pero menos extremo
lista.loc[lista['id_pais'] == "JP", 'peso'] *= 30

# Asia Oriental: refuerzo moderado
asia_oriental = ["CN", "KR", "TW", "HK", "PH"]
lista.loc[lista['id_pais'].isin(asia_oriental), 'peso'] *= 3

# EE.UU. con refuerzo fuerte
lista.loc[lista['id_pais'] == "US", 'peso'] *= 8

# México y Brasil con refuerzo moderado
latam = ["MX", "BR"]
lista.loc[lista['id_pais'].isin(latam), 'peso'] *= 2

# África y Caribe casi nulos
lista.loc[lista['continente'] == "África", 'peso'] *= 0.1
lista.loc[lista['continente'] == "Caribe", 'peso'] *= 0.1

# Normalizar pesos
lista['peso'] = lista['peso'] / lista['peso'].sum()

# Asignar países aleatoriamente con los pesos
n = len(df_limpio)
df_limpio['id_pais'] = lista.sample(n=n, weights=lista['peso'], replace=True)['id_pais'].tolist()

# Guardar
df_limpio.to_csv("Ventas_IBO_Gunpla_V3.0.csv", index=False)

print("🌏 Oceanía igual que América, EE.UU. con peso fuerte, Japón dominante, Asia reforzada, África y Caribe casi nulos.")
