"""Funciones del ejercicio 4."""

import matplotlib.pyplot as plt
import pandas as pd

from src import config


def FTR(data):
    """Devuelve el numero de partidos ganados en casa, fuera y empatados."""
    # Cuenta cuantos partidos terminan con victoria local, visitante o empate
    ftr = data["FTR"].value_counts()

    # Creamos un DataFrame con el resultado y su recuento
    ftr = pd.DataFrame({"Resultado": ftr.index, "Recuento": ftr.values})
    return ftr


def plot_FTR(ftr):
    """Representa graficamente los resultados de los partidos."""
    # Creamos la figura del grafico
    plt.figure(figsize=(10, 5))

    # Creamos el grafico de barras con los resultados
    plt.bar(ftr["Resultado"], ftr["Recuento"])
    plt.title("Resultados de los partidos")
    plt.xlabel("Resultado")
    plt.ylabel("Recuento")

    # Guardamos la grafica en la carpeta img
    plt.savefig(f"src/img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")
