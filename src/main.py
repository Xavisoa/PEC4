"""Punto de entrada principal del proyecto PEC4."""

import argparse

from src.exercises.ex1 import load_and_eda, plot_home_away_goals
from src.exercises.ex2 import total_matches, plot_matches_team_total
from src.exercises.ex3 import goals_distribution, plot_goals_distribution
from src.exercises.ex4 import FTR, plot_FTR
from src.exercises.ex5 import add_points, fun_total_points, alltime_winner
from src.exercises.ex6 import fun_total_goals, fun_total_goals_by_team, fun_summary_1996_2025, podium
from src.exercises.ex7 import graf

def parse_args():
    """Lee los argumentos indicados por terminal."""
    # Creamos un objeto ArgumentParser para gestionar los argumentos
    # que el usuario puede introducir al ejecutar el programa
    parser = argparse.ArgumentParser(description="PEC4 - Analisis de resultados historicos de La Liga")
    # Añadimos el argumento -ex para indicar hasta que ejercicio se ejecuta
    parser.add_argument(
        "-ex",
        # Convertimos el valor introducido a entero
        type=int,
        # Si el usuario no indica -ex, se ejecutarÃ¡n los 7 ejercicios
        default=7,
        # Solo se permiten valores entre 1 y 7
        choices=range(1, 8),
        # Texto que aparece cuando el usuario ejecute python main.py -h
        help="Ejecuta los ejercicios de forma incremental, de 1 a 7",
    )
    return parser.parse_args()


args = parse_args()

print("A continuacion se muestran las primeras y ultimas filas del dataset y las estadisticas basicas")
data = load_and_eda("src/data/LaLiga_Matches.csv")
plot_home_away_goals(data)

if args.ex >= 2:
    matches_team_total = total_matches(data)
    print("\nA continuacion se muestran los 10 equipos con mas partidos jugados")
    print(matches_team_total.head(10))

    max_matches = matches_team_total["Numero de partidos"].max()
    equipos_primera = matches_team_total[matches_team_total["Numero de partidos"] == max_matches]["Equipo"].tolist()
    print("Los equipos que siempre han estado en primera son:", equipos_primera)

    plot_matches_team_total(matches_team_total)

if args.ex >= 3:
    distr_goals_home, distr_goals_away = goals_distribution(data)
    print("\nDistribucion de goles locales")
    print(distr_goals_home)
    print("\nDistribucion de goles visitantes")
    print(distr_goals_away)

    plot_goals_distribution(distr_goals_home, distr_goals_away)

if args.ex >= 4:
    ftr = FTR(data)
    print("\nPartidos ganados en casa/fuera")
    print(ftr)

    local_wins = ftr[ftr["Resultado"] == "H"]["Recuento"].iloc[0]
    local_wins_percent = local_wins / ftr["Recuento"].sum() * 100
    print("Porcentaje de partidos ganados por los locales:", round(local_wins_percent, 2), "%")

    plot_FTR(ftr)

if args.ex >= 5:
    data = add_points(data)

    print("\nPrimeros valores con puntos por partido")
    print(data[["HomeTeam", "AwayTeam", "FTR", "points_home", "points_away"]].head(10))

    total_points, df_total_points = fun_total_points(data)
    print("\nPuntos totales por equipo")
    print(total_points.head(10))
    print(df_total_points.head(10))

    ganador = alltime_winner(df_total_points)
    print("Ganador historico:", ganador)

if args.ex >= 6:
    if "points_home" not in data.columns:
        data = add_points(data)
        total_points, df_total_points = fun_total_points(data)

    home_goals, away_goals, total_goals = fun_total_goals(data)

    print("\nGoles locales:", home_goals)
    print("Goles visitantes:", away_goals)
    print("Goles totales:", total_goals)

    home_goals_by_team, away_goals_by_team, total_goals_by_team = fun_total_goals_by_team(data)
    print(total_goals_by_team.head(10))

    summary_1996_2025 = fun_summary_1996_2025(
        df_total_points,
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team,
    )

    print(summary_1996_2025.head())
    podium(summary_1996_2025)

if args.ex >= 7:
    if "points_home" not in data.columns:
        data = add_points(data)
        total_points, df_total_points = fun_total_points(data)

    selected_teams = df_total_points["Equipo"].head(5).tolist()
    graf(data, selected_teams)