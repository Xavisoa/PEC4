from ex1 import load_and_eda, plot_home_away_goals
from ex2 import plot_matches_team_total, total_matches
from ex3 import goals_distribution, plot_goals_distribution
from ex4 import FTR, plot_FTR

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

# Ejecición de las funciones del ejecicio 3
distr_goals_home, distr_goals_away = goals_distribution(data)
print(distr_goals_home)
print("\n")
print(distr_goals_away)


#plot_goals_distribution(distr_goals_home, distr_goals_away)

# Ejecución de las funciones del ejercicio 4
ftr = FTR(data)
print(ftr)

plot_FTR(ftr)