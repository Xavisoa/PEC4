"""Funciones del ejercicio 7."""

import networkx as nx
import matplotlib.pyplot as plt

from src import config

def graf(data, selected_teams):
    ''' Crea un grafo con los enfrentamientos entre los 5 equipos seleccionados '''

    # Filtramos los partidos donde tanto el equipo local como el visitante
    # pertenecen a la lista de equipos seleccionados
    data_filtered = data[data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)]

    # Agrupamos por pareja de equipos (local y visitante)
    # y contamos cuÃ¡ntos partidos hay de cada combinaciÃ³n
    matches = (data_filtered.groupby(["HomeTeam", "AwayTeam"]).size().reset_index(name="Partidos"))

    # Creamos un grafo vacÃ­o utilizando la librerÃ­a networkx
    graph = nx.Graph()

    # AÃ±adimos cada equipo como un nodo del grafo
    for team in selected_teams:
        graph.add_node(team)

    # Recorremos todos los enfrentamientos encontrados
    for _, row in matches.iterrows():

        # Guardamos el nombre del equipo local
        home = row["HomeTeam"]

        # Guardamos el nombre del equipo visitante
        away = row["AwayTeam"]

        # Guardamos el nÃºmero de partidos disputados
        partidos = row["Partidos"]

        # Si ya existe una conexiÃ³n entre ambos equipos sumamos los partidos a la conexiÃ³n existente
        if graph.has_edge(home, away):
            graph[home][away]["weight"] += partidos

        # Si no existe la conexiÃ³n la creamos y guardamos el nÃºmero de partidos como peso de la conexiÃ³n
        else:
            graph.add_edge(home, away, weight=partidos)

    plt.figure(figsize=(10, 8))

    # Calculamos automÃ¡ticamente la posiciÃ³n de cada nodo
    # spring_layout distribuye los nodos intentando que no se solapen
    layout = nx.spring_layout(graph)

    # Dibujamos el grafo
    nx.draw(graph, layout, with_labels=True, node_size=3000)

    # Obtenemos el peso de cada conexiÃ³n (nÃºmero de partidos)
    labels = nx.get_edge_attributes(graph, "weight")

    # Dibujamos sobre cada lÃ­nea el nÃºmero de enfrentamientos
    nx.draw_networkx_edge_labels(graph, layout, edge_labels=labels)

    # AÃ±adimos un tÃ­tulo al grÃ¡fico
    plt.title("Enfrentamientos entre los 5 mejores equipos")

    # Guardamos la imagen generada
    plt.savefig(f"src/img/grafo_{config.nom_alumne}_{config.date_time}.png")
