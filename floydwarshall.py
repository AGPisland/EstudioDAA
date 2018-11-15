import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def FloydWarshall(G):
    distance = {}
    previous = {}
    
    for node_pivot in G.node:
        distance[node_pivot] = {}
        previous[node_pivot] = {}      
        for node_target in G.node:
            if G.has_edge(node_pivot, node_target):
                distance[node_pivot][node_target] = G[node_pivot][node_target]['weight']
                previous[node_pivot][node_target] = node_pivot
            else:
                distance[node_pivot][node_target] = float('inf')
                previous[node_pivot][node_target] = -1
        distance[node_pivot][node_pivot] = 0
        
    for node_inter in G.node:
        for node_pivot in G.node:
            for node_target in G.node:
                current = distance[node_pivot][node_inter] + distance[node_inter][node_target]
                if current < distance[node_pivot][node_target]:
                    distance[node_pivot][node_target] = current
                    previous[node_pivot][node_target] = previous[node_inter][node_target]
                
    return distance, previous
    
    #distance[edge] = G.degree(node)
if __name__ == '__main__':
    M = np.array([[0,7,9,0,0,14],    
                  [7,0,10,15,0,0],
                  [9,10,0,11,0,2],
                  [0,15,11,0,6,3],
                  [0,0,0,6,0,9],
                  [14,0,2,3,9,0]])
    G = nx.Graph(M)
    pos = nx.spring_layout(G)
    labels = {}
    cycle = 0
    
    for idx, node in enumerate(G.nodes()):
        labels[node] = idx
    for edgei,edgee in G.edges():
        labels[edgei][edgee] = G[edgei][edgee]['weight']
    #Nodes
    nx.draw_networkx_nodes(G, pos,
                       node_color='r',
                       node_size=500,
                       alpha=0.8)
    #Edges
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    #Labels
    nx.draw_networkx_labels(G, pos, labels, font_size=16)
    nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G))
    plt.show()
    
    distance, previous = FloydWarshall(G)
    print("Rutas:\n")
    for p in previous: print("{} {} \n".format(p, previous[p]))
    print("----------------\n")
    print("Distancias:\n")
    for d in distance: print("{} {} \n".format(d, distance[d])) 
          
