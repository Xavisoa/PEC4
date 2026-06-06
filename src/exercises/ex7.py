import networkx as nx
import matplotlib.pyplot as plt

import config

def graf(data, selected_teams):
    ''' Crea un grafo con los enfrentamientos entre los 5 equipos seleccionados '''

    # Filtramos los partidos donde tanto el equipo local como el visitante
    # pertenecen a la lista de equipos seleccionados
    data_filtered = data[data["HomeTeam"].isin(selected_teams) & data["AwayTeam"].isin(selected_teams)]

    # Agrupamos por pareja de equipos (local y visitante)
    # y contamos cuántos partidos hay de cada combinación
    matches = (data_filtered.groupby(["HomeTeam", "AwayTeam"]).size().reset_index(name="Partidos"))

    # Creamos un grafo vacío utilizando la librería networkx
    G = nx.Graph()

    # Añadimos cada equipo como un nodo del grafo
    for team in selected_teams:
        G.add_node(team)

    # Recorremos todos los enfrentamientos encontrados
    for i, row in matches.iterrows():

        # Guardamos el nombre del equipo local
        home = row["HomeTeam"]

        # Guardamos el nombre del equipo visitante
        away = row["AwayTeam"]

        # Guardamos el número de partidos disputados
        partidos = row["Partidos"]

        # Si ya existe una conexión entre ambos equipos sumamos los partidos a la conexión existente
        if G.has_edge(home, away):
            G[home][away]["weight"] += partidos

        # Si no existe la conexión la creamos y guardamos el número de partidos como peso de la conexión
        else:
            G.add_edge(home, away, weight=partidos)

    plt.figure(figsize=(10, 8))

    # Calculamos automáticamente la posición de cada nodo
    # spring_layout distribuye los nodos intentando que no se solapen
    layout = nx.spring_layout(G)

    # Dibujamos el grafo
    nx.draw(G, layout, with_labels=True, node_size=3000)

    # Obtenemos el peso de cada conexión (número de partidos)
    labels = nx.get_edge_attributes(G, "weight")

    # Dibujamos sobre cada línea el número de enfrentamientos
    nx.draw_networkx_edge_labels(G, layout, edge_labels=labels)

    # Añadimos un título al gráfico
    plt.title("Enfrentamientos entre los 5 mejores equipos")

    # Guardamos la imagen generada
    plt.savefig(f"img/grafo_{config.nom_alumne}_{config.date_time}.png")