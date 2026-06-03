import matplotlib.pyplot as plt
import pandas as pd

import config

def goals_distribution(data):
    ''' Devuelve la distribución de goles marcados por equipos locales y visitantes. '''

    # Cuenta cuántos partidos tienen cada número de goles locales y los ordena de forma ascendente
    distr_goals_home = data["FTHG"].value_counts().sort_index()

    # Cuenta cuántos partidos tienen cada número de goles visitantes y los ordena de forma ascendente
    distr_goals_away = data["FTAG"].value_counts().sort_index()

    # Convierte las series en DataFrames
    distr_goals_home = distr_goals_home.to_frame(name="Distribución de goles local")
    distr_goals_away = distr_goals_away.to_frame(name="Distribución de goles visitante")

    return distr_goals_home, distr_goals_away

def plot_goals_distribution(distr_goals_home, distr_goals_away):
    ''' Representa la distribución de goles de locales y visitantes '''
    plt.figure(figsize=(10, 6))
    plt.plot(distr_goals_home.index,distr_goals_home["Distribución de goles local"],label="Goles locales")
    plt.plot(distr_goals_away.index,distr_goals_away["Distribución de goles visitante"],label="Goles visitantes")
    plt.title("Distribución de goles")
    plt.xlabel("Número de goles")
    plt.ylabel("Número de partidos")
    plt.xticks(range(0, 11))
    plt.legend()
    plt.savefig(f"img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")