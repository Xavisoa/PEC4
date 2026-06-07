"""Funciones del ejercicio 7."""

import matplotlib.pyplot as plt
import networkx as nx

from src import config


def graf(data, selected_teams):
    """Crea un grafo con los enfrentamientos entre los equipos seleccionados."""
    # Filtramos los partidos donde local y visitante estan en la lista de equipos seleccionados
    data_filtered = data[
        data["HomeTeam"].isin(selected_teams)
        & data["AwayTeam"].isin(selected_teams)
    ]

    # Agrupamos por pareja de equipos y contamos cuantos partidos han jugado
    matches = data_filtered.groupby(["HomeTeam", "AwayTeam"]).size().reset_index(name="Partidos")

    # Creamos un grafo vacio
    graph = nx.Graph()

    # Anadimos cada equipo como nodo
    for team in selected_teams:
        graph.add_node(team)

    # Recorremos los enfrentamientos y creamos las conexiones
    for _, row in matches.iterrows():
        home = row["HomeTeam"]
        away = row["AwayTeam"]
        partidos = row["Partidos"]

        # Si la conexion ya existe, sumamos los partidos
        if graph.has_edge(home, away):
            graph[home][away]["weight"] += partidos
        else:
            # Si no existe, creamos la conexion con el numero de partidos
            graph.add_edge(home, away, weight=partidos)

    # Creamos la figura y calculamos la posicion de los nodos
    plt.figure(figsize=(10, 8))
    layout = nx.spring_layout(graph)

    # Dibujamos el grafo con los nombres de los equipos
    nx.draw(graph, layout, with_labels=True, node_size=3000)

    # Obtenemos y dibujamos las etiquetas de las conexiones
    labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, layout, edge_labels=labels)
    plt.title("Enfrentamientos entre los 5 mejores equipos")

    # Guardamos la grafica en la carpeta img
    plt.savefig(f"src/img/grafo_{config.nom_alumne}_{config.date_time}.png")
