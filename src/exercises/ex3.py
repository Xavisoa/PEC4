"""Funciones del ejercicio 3."""

import matplotlib.pyplot as plt

from src import config


def goals_distribution(data):
    """Devuelve la distribucion de goles marcados por locales y visitantes."""
    # Cuenta cuantos partidos tienen cada numero de goles locales
    distr_goals_home = data["FTHG"].value_counts().sort_index()

    # Cuenta cuantos partidos tienen cada numero de goles visitantes
    distr_goals_away = data["FTAG"].value_counts().sort_index()

    # Convertimos las series en DataFrames y damos nombre a las columnas
    distr_goals_home = distr_goals_home.to_frame(name="Distribucion de goles local")
    distr_goals_away = distr_goals_away.to_frame(name="Distribucion de goles visitante")

    return distr_goals_home, distr_goals_away


def plot_goals_distribution(distr_goals_home, distr_goals_away):
    """Representa la distribucion de goles de locales y visitantes."""
    # Creamos la figura del grafico
    plt.figure(figsize=(10, 6))

    # Dibujamos la distribucion de goles de los equipos locales
    plt.plot(
        distr_goals_home.index,
        distr_goals_home["Distribucion de goles local"],
        label="Goles locales",
    )

    # Dibujamos la distribucion de goles de los equipos visitantes
    plt.plot(
        distr_goals_away.index,
        distr_goals_away["Distribucion de goles visitante"],
        label="Goles visitantes",
    )

    # Anadimos titulo, etiquetas y leyenda
    plt.title("Distribucion de goles")
    plt.xlabel("Numero de goles")
    plt.ylabel("Numero de partidos")
    plt.xticks(range(0, 11))
    plt.legend()

    # Guardamos la grafica en la carpeta img
    plt.savefig(f"src/img/grafica_ex3_{config.nom_alumne}_{config.date_time}.png")
