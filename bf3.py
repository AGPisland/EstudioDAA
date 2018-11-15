import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def BellmanFord(graph, initial_node, final_node):
    #Variable's initialization
    distance = {}
    previous = {}

    for node in range(len(graph)):
        distance[node] = float('inf')
        
    distance[initial_node] = 0
    #Edge's relaxation
    for _ in range(len(graph) - 1):
        for node_pivot in range(len(graph)):
            for node_target in range(len(graph)):
                if graph[node_pivot, node_target] != 0 and distance[node_pivot] + graph[node_pivot, node_target] < distance[node_target]:
                    distance[node_target] = distance[node_pivot] + graph[node_pivot, node_target]
                    previous[node_target] = node_pivot
    #Checking if the algorithm runs into a negative cycle
    for node_pivot in range(len(graph)):
            for node_target in range(len(graph)):
                if graph[node_pivot, node_target] != 0 and distance[node_pivot] + graph[node_pivot, node_target] < distance[node_target]: 
                    assert distance[node_target] <= distance[node_pivot] + graph[node_pivot][node_target], "Ciclo negativo"
    
    return(distance[final_node], Path(previous, initial_node, final_node))

def Path(previous, initial_node, final_node):
    route = [final_node]
    
    while final_node is not initial_node:
        route.append(previous[final_node])
        final_node = previous[final_node]
        
    route.reverse()
    return(route)
   
    
if __name__ == '__main__':
    """M = np.array([[0,3,4,0,0,0],
                  [3,0,9,2,2,0],
                  [4,9,0,5,0,0],
                  [0,-2,-5,0,3,3],
                  [0,2,0,3,0,1],
                  [0,0,0,3,1,0]])"""
    M = np.array([[0,7,9,0,0,14],   #Testing using the same graph I used in the Dijkstra's algorithm 
                  [7,0,10,15,0,0],
                  [9,10,0,11,0,2],
                  [0,15,11,0,6,3],
                  [0,0,0,6,0,9],
                  [14,0,2,0,9,0]])
    G = nx.Graph(M)
    pos = nx.spring_layout(G)
    labels = {}
    cycle = 0
    
    for idx, node in enumerate(G.nodes()):
        labels[node] = idx
    #Nodes
    nx.draw_networkx_nodes(G, pos,
                       node_color='r',
                       node_size=500,
                       alpha=0.8)
    #Edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    #Labels
    nx.draw_networkx_labels(G, pos, labels, font_size=16)
    plt.show()
    
    while cycle is 0:
        x = int(input("Nodo de inicio: "))
        y = int(input("Nodo final: "))
        distance, route = BellmanFord(M, x, y)
        print("La distancia es {} y la ruta es {}".format(distance, route))
        cycle = int(input("0 para continuar, de lo contrario presione otra tecla: "))

    