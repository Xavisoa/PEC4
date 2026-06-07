"""Funciones del ejercicio 5."""

import pandas as pd


def add_points(data):
    """Anade las columnas points_home y points_away al DataFrame."""
    # Creamos las columnas de puntos para locales y visitantes con valor inicial 0
    data["points_home"] = 0
    data["points_away"] = 0

    # Si gana el equipo local, recibe 3 puntos
    data.loc[data["FTR"] == "H", "points_home"] = 3

    # Si gana el equipo visitante, recibe 3 puntos
    data.loc[data["FTR"] == "A", "points_away"] = 3

    # Si hay empate, cada equipo recibe 1 punto
    data.loc[data["FTR"] == "D", "points_home"] = 1
    data.loc[data["FTR"] == "D", "points_away"] = 1

    return data


def fun_total_points(data):
    """Suma los puntos totales obtenidos por cada equipo."""
    # Agrupamos por equipo local y sumamos los puntos conseguidos en casa
    home_points = data.groupby("HomeTeam")["points_home"].sum()

    # Agrupamos por equipo visitante y sumamos los puntos conseguidos fuera
    away_points = data.groupby("AwayTeam")["points_away"].sum()

    # Sumamos los puntos como local y como visitante
    total_points = home_points.add(away_points)

    # Ordenamos los equipos de mayor a menor puntuacion
    total_points = total_points.sort_values(ascending=False)

    # Creamos un DataFrame con el equipo y sus puntos totales
    df_total_points = pd.DataFrame({
        "Equipo": total_points.index,
        "Puntos": total_points.values,
    })

    return total_points, df_total_points


def alltime_winner(df_total_points):
    """Devuelve el equipo con mas puntos historicos."""
    # Como el DataFrame esta ordenado, el primer equipo es el ganador historico
    return df_total_points.iloc[0]["Equipo"]
