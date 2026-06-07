"""Funciones del ejercicio 2."""

import matplotlib.pyplot as plt
import pandas as pd

from src import config


def total_matches(data):
    """Devuelve un DataFrame con el numero total de partidos jugados por cada equipo."""
    # Cuenta cuantos partidos ha jugado cada equipo como local
    home_matches = data["HomeTeam"].value_counts()

    # Cuenta cuantos partidos ha jugado cada equipo como visitante
    away_matches = data["AwayTeam"].value_counts()

    # Sumamos los partidos como local y visitante
    matches_team_total = home_matches.add(away_matches, fill_value=0)

    # Ordenamos los equipos de mayor a menor numero de partidos
    matches_team_total = matches_team_total.sort_values(ascending=False)

    # Creamos un DataFrame con el nombre del equipo y el total de partidos
    matches_team_total = pd.DataFrame({
        "Equipo": matches_team_total.index,
        "Numero de partidos": matches_team_total.values,
    })

    return matches_team_total


def plot_matches_team_total(matches_team_total):
    """Crea un grafico de barras con la relacion de equipos y partidos jugados."""
    # Creamos la figura del grafico
    plt.figure(figsize=(14, 6))

    # Creamos el grafico de barras con los equipos y sus partidos totales
    plt.bar(matches_team_total["Equipo"], matches_team_total["Numero de partidos"])
    plt.title("Partidos totales por equipo")
    plt.xlabel("Equipo")
    plt.ylabel("Numero de partidos total")

    # Rotamos los nombres de los equipos para que se puedan leer mejor
    plt.xticks(rotation=90)
    plt.tight_layout()

    # Guardamos la grafica en la carpeta img
    plt.savefig(f"src/img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
