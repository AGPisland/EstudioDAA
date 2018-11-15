import numpy as np 
import networkx as nx 
import matplotlib.pyplot as plt

def Dibujar_Grafo(Matrix):
    G=nx.Graph(Matrix)
    pos=nx.spring_layout(G)
    labels={}
    for idx, node in enumerate(G.nodes()):
        labels[node]=idx
        print(node)


    nx.draw_networkx_nodes(G, pos,
                        node_color='r',
                        node_size=500,
                        alpha=0.8)
    nx.draw_networkx_edges(G,pos, width=1.0,alpha=0.5)
    nx.draw_networkx_labels(G, pos, labels, font_size=16)
    plt.show()

if __name__ is '__main__':
    M=np.array([[0,1,2,3,4,5],
                [1,0,3,4,5,6],
                [2,3,0,5,6,7],
                [3,4,5,0,7,8],
                [4,5,6,7,0,9],
                [5,6,7,8,9,0]])
    Dibujar_Grafo(M)

