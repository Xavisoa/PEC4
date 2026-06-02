import matplotlib.pyplot as plt
import pandas as pd

import config


def load_and_eda(file):
    """Se cargan los datos del DataFrame, se limpian y se realiza un primer análisis."""
    df = pd.read_csv(file)
    df = df.drop(columns=["HTHG", "HTAG", "HTR"])
    print(df.head())
    print(df.tail())
    print(df.describe())
    return df


def plot_home_away_goals(df):
    """Se crea un boxplot con los goles marcados por los equipos de casa y por los equipos de fuera"""
    plt.figure(figsize=(8, 5))
    plt.boxplot([df["FTHG"], df["FTAG"]])
    plt.xticks([1, 2], ["Goles casa", "Goles fuera"])
    plt.title("Distribución de goles")
    plt.ylabel("Goles")
    plt.savefig(f"img/grafica_ex1_{config.nom_alumne}_{config.date_time}.png")
    plt.show()
