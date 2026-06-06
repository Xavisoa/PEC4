"""Funciones del ejercicio 3."""

import matplotlib.pyplot as plt

from src import config

def goals_distribution(data):
    ''' Devuelve la distribuciÃ³n de goles marcados por equipos locales y visitantes. '''

    # Cuenta cuÃ¡ntos partidos tienen cada nÃºmero de goles locales y los ordena de forma ascendente
    distr_goals_home = data["FTHG"].value_counts().sort_index()

    # Cuenta cuÃ¡ntos partidos tienen cada nÃºmero de goles visitantes y los ordena de forma ascendente
    distr_goals_away = data["FTAG"].value_counts().sort_index()

    # Convierte las series en DataFrames
    distr_goals_home = distr_goals_home.to_frame(name="DistribuciÃ³n de goles local")
    distr_goals_away = distr_goals_away.to_frame(name="DistribuciÃ³n de goles visitante")

    return distr_goals_home, distr_goals_away

def plot_goals_distribution(distr_goals_home, distr_goals_away):
    ''' Representa la distribuciÃ³n de goles de locales y visitantes '''
    plt.figure(figsize=(10, 6))
    plt.plot(distr_goals_home.index,distr_goals_home["DistribuciÃ³n de goles local"],label="Goles locales")
    plt.plot(distr_goals_away.index,distr_goals_away["DistribuciÃ³n de goles visitante"],label="Goles visitantes")
    plt.title("DistribuciÃ³n de goles")
    plt.xlabel("NÃºmero de goles")
    plt.ylabel("NÃºmero de partidos")
    plt.xticks(range(0, 11))
    plt.legend()
    plt.savefig(f"src/img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
