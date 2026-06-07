"""Funciones del ejercicio 6."""

import matplotlib.pyplot as plt
import pandas as pd

from src import config


def fun_total_goals(data):
    """Devuelve el total de goles locales, visitantes y totales."""
    # Sumamos todos los goles marcados por los equipos locales
    home_goals = data["FTHG"].sum()

    # Sumamos todos los goles marcados por los equipos visitantes
    away_goals = data["FTAG"].sum()

    # Sumamos goles locales y visitantes
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data):
    """Devuelve los goles marcados por cada equipo como local, visitante y total."""
    # Agrupamos por equipo local y sumamos los goles marcados en casa
    home_goals_by_team = data.groupby("HomeTeam")["FTHG"].sum()

    # Agrupamos por equipo visitante y sumamos los goles marcados fuera
    away_goals_by_team = data.groupby("AwayTeam")["FTAG"].sum()

    # Sumamos los goles como local y como visitante
    total_goals_by_team = home_goals_by_team.add(away_goals_by_team)

    # Convertimos las series en DataFrames
    home_goals_by_team = home_goals_by_team.to_frame(name="Goles local")
    away_goals_by_team = away_goals_by_team.to_frame(name="Goles visitante")
    total_goals_by_team = total_goals_by_team.to_frame(name="Goles totales")

    return home_goals_by_team, away_goals_by_team, total_goals_by_team


def fun_summary_1996_2025(
    total_points_by_team,
    home_goals_by_team,
    away_goals_by_team,
    total_goals_by_team,
):
    """Une puntos, goles locales, goles visitantes y goles totales en un DataFrame."""
    # Concatenamos los DataFrames por columnas usando el equipo como indice
    summary_1996_2025 = pd.concat([
        total_points_by_team.set_index("Equipo"),
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team,
    ], axis=1)

    return summary_1996_2025


def podium(summary_1996_2025):
    """Representa el podio de los tres mejores equipos."""
    # Ordenamos por puntos y seleccionamos los tres primeros equipos
    podium_df = summary_1996_2025.sort_values(by="Puntos", ascending=False).head(3)

    # Colocamos el primero en el centro, el segundo a la izquierda y el tercero a la derecha
    equipos = [podium_df.index[1], podium_df.index[0], podium_df.index[2]]
    alturas = [2, 3, 1]

    # Creamos el grafico de barras con forma de podio
    plt.figure(figsize=(8, 6))
    plt.bar([0, 1, 2], alturas, color=["silver", "gold", "saddlebrown"])

    # Escribimos el nombre de cada equipo encima de su barra
    plt.text(0, 2, equipos[0], ha="center")
    plt.text(1, 3, equipos[1], ha="center")
    plt.text(2, 1, equipos[2], ha="center")
    plt.title("Podio historico")

    # Guardamos la grafica en la carpeta img
    plt.savefig(f"src/img/podium_{config.nom_alumne}_{config.date_time}.png")
