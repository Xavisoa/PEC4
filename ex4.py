import pandas as pd
import matplotlib.pyplot as plt

import config

def FTR(data):
    ''' Devuelve el número de partidos ganados en casa/fuera. '''
    # Cuenta cuantas victorias, empates y derrotas
    ftr = data["FTR"].value_counts()
    # Creamos el DataFrame con el resultado como indice y el recuento como valores
    ftr = pd.DataFrame({"Resultado": ftr.index, "Recuento": ftr.values})
    return ftr

def plot_FTR(ftr):
    ''' Representación grafica de los partidos ganados por locales y visitantes'''
    plt.figure(figsize=(10, 5))
    plt.bar(ftr["Resultado"], ftr["Recuento"])
    plt.title("Resultados de los partidos")
    plt.xlabel("Resultado")
    plt.ylabel("Recuento")
    plt.savefig(f"img/grafica_ex4_{config.nom_alumne}_{config.date_time}.png")