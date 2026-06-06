
"""Funciones del ejercicio 2."""

import matplotlib.pyplot as plt
import pandas as pd

from src import config


def total_matches(data):
    ''' Devuelve un dataframe con el nÃºmero total de partidos jugados por cada equipo '''

    # Cuenta cuÃ¡ntos partidos ha jugado cada equipo como local con value_counts()
    home_matches = data["HomeTeam"].value_counts()
    # Cuenta cuÃ¡ntos partidos ha jugado cada equipo como visitante con value_counts()
    away_matches = data["AwayTeam"].value_counts()

    # Suma los partidos como local y visitante para obtener el total
    matches_team_total = home_matches.add(away_matches, fill_value=0)
    # Ordena los equipos con mayor numero de partidos a menos
    matches_team_total = matches_team_total.sort_values(ascending=False)

    # Creamos el dataframe para mostrar los equipos y el nÃºmero de partidos. Con .index mostramos el nombre de
    # los equipos y con .values vemos los valores
    matches_team_total = pd.DataFrame({
        "Equipo": matches_team_total.index,
        "NÃºmero de partidos": matches_team_total.values,
    })

    return matches_team_total

# Para la creaciÃ³n de este grafico se utiliza un grafico de barras
def plot_matches_team_total(matches_team_total):
    ''' Crea un grafico de barras con la relaciÃ³n de equipos y partidos jugados '''
    plt.figure(figsize=(14, 6))
    # Utilizamos los datos creados con la funcion de total_matches
    plt.bar(matches_team_total["Equipo"], matches_team_total["NÃºmero de partidos"])
    plt.title("Partidos totales por equipo")
    plt.xlabel("Equipo")
    plt.ylabel("NÃºmero de partidos total")
    # Se rotan los nombres para que se puedan ver bien ene grafico
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f"src/img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
