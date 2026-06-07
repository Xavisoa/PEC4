"""Funciones del ejercicio 1."""

import matplotlib.pyplot as plt
import pandas as pd

from src import config


def load_and_eda(file):
    """Carga los datos del DataFrame, los limpia y realiza un primer analisis."""
    # Cargamos el dataset con pandas
    data = pd.read_csv(file)

    # Eliminamos las columnas relacionadas con el resultado al descanso
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])

    # Mostramos las primeras filas del DataFrame
    print("Primeras filas")
    print(data.head())
    print("\n")

    # Mostramos las ultimas filas del DataFrame
    print("Ultimas filas")
    print(data.tail())
    print("\n")

    # Mostramos las estadisticas basicas de las columnas numericas
    print("Estadisticas basicas")
    print(data.describe())
    return data


def plot_home_away_goals(data):
    """Crea un boxplot con los goles marcados en casa y fuera."""
    # Creamos la figura donde se representara el grafico
    plt.figure(figsize=(8, 5))

    # Creamos un boxplot comparando goles de equipos locales y visitantes
    plt.boxplot([data["FTHG"], data["FTAG"]])
    plt.xticks([1, 2], ["Goles casa", "Goles fuera"])

    # Anadimos titulo y etiqueta del eje Y
    plt.title("Distribucion de goles")
    plt.ylabel("Goles")

    # Guardamos la grafica en la carpeta img
    plt.savefig(f"src/img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
