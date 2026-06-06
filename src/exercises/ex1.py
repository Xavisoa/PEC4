import matplotlib.pyplot as plt
import pandas as pd
import config


def load_and_eda(file):
    """Se cargan los datos del DataFrame, se limpian y se realiza un primer análisis."""
    data = pd.read_csv(file)
    data = data.drop(columns=["HTHG", "HTAG", "HTR"])
    print("Primeras filas")
    print(data.head())
    print("\n")
    print("Ultimas filas")
    print(data.tail())
    print("\n")
    print("Estadisticas basicas")
    print(data.describe())
    return data


def plot_home_away_goals(data):
    """Se crea un boxplot con los goles marcados por los equipos de casa y por los equipos de fuera"""
    plt.figure(figsize=(8, 5))
    plt.boxplot([data["FTHG"], data["FTAG"]])
    plt.xticks([1, 2], ["Goles casa", "Goles fuera"])
    plt.title("Distribución de goles")
    plt.ylabel("Goles")
    plt.savefig(f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
