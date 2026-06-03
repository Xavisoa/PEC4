
import matplotlib.pyplot as plt
import pandas as pd

import config


def total_matches(data):
    ''' Devuelve un dataframe con el número total de partidos jugados por cada equipo '''

    # Cuenta cuántos partidos ha jugado cada equipo como local con value_counts()
    home_matches = data["HomeTeam"].value_counts()
    # Cuenta cuántos partidos ha jugado cada equipo como visitante con value_counts()
    away_matches = data["AwayTeam"].value_counts()

    # Suma los partidos como local y visitante para obtener el total
    matches_team_total = home_matches.add(away_matches)
    # Ordena los equipos con mayor numero de partidos a menos
    matches_team_total = matches_team_total.sort_values(ascending=False)

    # Creamos el dataframe para mostrar los equipos y el número de partidos. Con .index mostramos el nombre de
    # los equipos y con .values vemos los valores
    matches_team_total = pd.DataFrame({"Equipo": matches_team_total.index, "Número de partidos": matches_team_total.values})

    return matches_team_total

# Para la creación de este grafico se utiliza un grafico de barras
def plot_matches_team_total(matches_team_total):
    ''' Crea un grafico de barras con la relación de equipos y partidos jugados '''
    plt.figure(figsize=(14, 6))
    # Utilizamos los datos creados con la funcion de total_matches
    plt.bar(matches_team_total["Equipo"], matches_team_total["Número de partidos"])
    plt.title("Partidos totales por equipo")
    plt.xlabel("Equipo")
    plt.ylabel("Número de partidos total")
    # Se rotan los nombres para que se puedan ver bien ene grafico
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(f"img/grafica_ex2_{config.nom_alumne}_{config.date_time}.png")
