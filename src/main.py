from ex1 import load_and_eda, plot_home_away_goals
from ex2 import plot_matches_team_total, total_matches
from ex3 import goals_distribution, plot_goals_distribution
from ex4 import FTR, plot_FTR
from ex5 import add_points, fun_total_points, alltime_winner
from ex6 import fun_total_goals, fun_total_goals_by_team, fun_summary_1996_2025, podium
from ex7 import graf

# Ejecución de las funciones del ejercicio 1
print("A continuación se muestran las primeras y utimas filas del dasat y las estadisticas basicas")
data = load_and_eda("data/LaLiga_Matches.csv")
#plot_home_away_goals(data)

# Ejecución de las funciones del ejecicio 2
matches_team_total = total_matches(data)
print("\n")
print(" A continuación se muestran los 10 equipos con mas partidos jugados")
print(matches_team_total.head(10))

# Para poder ver que equipos han estado siempre en primera se hace una lista con los equipos con el
# máximo número de partidos jugado
print("\n")

# Obtenemos el número máximo de partidos jugados
max_matches = matches_team_total["Número de partidos"].max()
# Obtenemos los equipos cuyo número de partidos es igual al máximo
# y convertimos el resultado en una lista
equipos_primera = matches_team_total[matches_team_total["Número de partidos"] == max_matches]["Equipo"].tolist()
print("Los equipos que siempre han estado en primera son:", equipos_primera)

#plot_matches_team_total(matches_team_total)

print("\n")

# Ejecución de las funciones del ejecicio 3
distr_goals_home, distr_goals_away = goals_distribution(data)
print(distr_goals_home)
print("\n")
print(distr_goals_away)


#plot_goals_distribution(distr_goals_home, distr_goals_away)

print("\n")

# Ejecución de las funciones del ejercicio 4
ftr = FTR(data)
print("Partidos ganados en casa/fuera")
print(ftr)

plot_FTR(ftr)

print("\n")

# Ejecucion de las funciones del ejecicio 5

data = add_points(data)

print(data[["HomeTeam", "AwayTeam", "FTR",
            "points_home", "points_away"]].head(10))

print("\n")

total_points, df_total_points = fun_total_points(data)

print(total_points.head(10))
print(df_total_points.head(10))

print("\n")

ganador = alltime_winner(df_total_points)

print("Ganador histórico:", ganador)

print("\n")

# Ejecutamos las funciones del ejercicio 6

home_goals, away_goals, total_goals = fun_total_goals(data)

print("Goles locales:", home_goals)
print("Goles visitantes:", away_goals)
print("Goles totales:", total_goals)


home_goals_by_team, away_goals_by_team, total_goals_by_team = (fun_total_goals_by_team(data))

print(total_goals_by_team.head(10))

summary_1996_2025 = fun_summary_1996_2025(df_total_points, home_goals_by_team, away_goals_by_team, total_goals_by_team)

print(summary_1996_2025.head())

podium(summary_1996_2025)

print("\n")

# Ejecución de las funciones del ejercicio 7

# Seleccionamos los 5 primeros equipos
selected_teams = df_total_points["Equipo"].head(5).tolist()
graf(data, selected_teams)