"""Funciones para leer y guardar datasets y gráficos del proyecto.

Las rutas se calculan a partir de la ubicación de este archivo (src/utils),
así funcionan igual desde cualquier notebook, esté en la carpeta que esté.
"""
import os

import pandas as pd
import matplotlib.pyplot as plt

# src/  (la carpeta que contiene a utils)
CARPETA_SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_DATOS = os.path.join(CARPETA_SRC, "data")
CARPETA_GRAFICOS = os.path.join(CARPETA_SRC, "visualizaciones")


def cargar_dataset(nombre, carpeta="Mergeados"):
    """Lee un CSV de src/data/<carpeta>/ y devuelve un DataFrame."""
    ruta = os.path.join(CARPETA_DATOS, carpeta, nombre)
    return pd.read_csv(ruta)


def guardar_dataset(df, nombre, carpeta="Mergeados", index=False):
    """Guarda un DataFrame como CSV en src/data/<carpeta>/."""
    os.makedirs(os.path.join(CARPETA_DATOS, carpeta), exist_ok=True)
    ruta = os.path.join(CARPETA_DATOS, carpeta, nombre)
    df.to_csv(ruta, index=index)
    print("Guardado:", ruta)


def guardar_grafico(nombre):
    """Guarda el gráfico actual como PNG en src/visualizaciones/."""
    os.makedirs(CARPETA_GRAFICOS, exist_ok=True)
    ruta = os.path.join(CARPETA_GRAFICOS, nombre)
    plt.savefig(ruta, bbox_inches="tight")
    print("Guardado:", ruta)
