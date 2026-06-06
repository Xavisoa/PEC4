"""Funciones del ejercicio 5."""

import pandas as pd


def add_points(data):
    ''' AÃƒÂ±ade las columnas points_home y points_away al DataFrame con los puntos obtenidos en cada partido '''

    # Creamos las columnas de puntos de locales y visitantes a 0
    data["points_home"] = 0
    data["points_away"] = 0

    # Con .loc buscamos en la columna FTR el valor H y le pones a la columna points_home el valore de 3
    data.loc[data["FTR"] == "H", "points_home"] = 3

    # Lo mismo con A
    data.loc[data["FTR"] == "A", "points_away"] = 3

    # Hacemos lo mismo para el equipo local cuando hay empate y le damos un punto
    data.loc[data["FTR"] == "D", "points_home"] = 1

    # Lo mismo para el equipo visitnate
    data.loc[data["FTR"] == "D", "points_away"] = 1

    # Devuelve el DataFrame con las nuevas columnas aÃƒÂ±adidas
    return data


def fun_total_points(data):
    ''' Suma los puntos totales obtenidos por cada equipo '''

    # Con groupby agrupamos todos los partidos por equipo local y con sum sumamos todos los puntos
    home_points = data.groupby("HomeTeam")["points_home"].sum()

    # Hacemos lo mismo para los equipos visitantes
    away_points = data.groupby("AwayTeam")["points_away"].sum()

    # Sumamos los puntos totales
    total_points = home_points.add(away_points)

    # Ordenamos los equipos de mayor a menor nÃƒÂºmero de puntos
    total_points = total_points.sort_values(ascending=False)

    # Creamos un DataFrame utilizando los nombres de los equipos en el ÃƒÂ­ndice y los puntos como valores
    df_total_points = pd.DataFrame({"Equipo": total_points.index, "Puntos": total_points.values})

    # Devolvemos la seria y el DataFrame creados
    return total_points, df_total_points

def alltime_winner(df_total_points):
    ''' Devuelve el equipo con mÃƒÂ¡s puntos histÃƒÂ³ricos '''

    # Como df_total_points estÃƒÂ¡ ordenado del equipo con mÃƒÂ¡s puntos al equipo con menos
    # con iloc[0] seleccionamos el primer equipo
    return df_total_points.iloc[0]["Equipo"]
