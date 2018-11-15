import networkx as nx
import numpy as np
from heapq import heappush, heappop

def Dijkstra(G, initial_node, final_node):
    distance = {initial_node: 0}
    previous = {}
    nodes = set(G.nodes())
    heap = []
    min = 0
    current_distance = 0


    for node in nodes:
        if node is not initial_node:
            distance[node] = 0#float('inf')
        heappush(heap, node)
    #print(heap, distance)
    while heap:
        min = heappop(heap)
        #print('pila: ',min, ' contador: ', contador)
        for node in nodes:
            #print('el nodo origen ', min, ' tiene ruta hacia el nodo ', node)
            if G.has_edge(min, node) and G[min][node]['weight'] != 0:
                #print(' TIENE RUTA CON COSTO: ', G[min][node]['weight'])
                current_distance = distance[min] + G[min][node]['weight']
                #print(' la ponderacion desde origen es de: ', current_distance) 
                #print(current_distance, ' es menor que ', distance[node])
                if current_distance > distance[node]:
                    #print('true')
                    #10<inf ::: true
                    distance[node] = current_distance
                    previous[node] = min
                    heappush(heap, node)
                    #print(distance, previous, heap)
    return distance[final_node] #, Path(previous, initial_node, final_node)

def Path(previous, initial_node, final_node):
    route = [final_node]
    
    while final_node is not initial_node:
        route.append(previous[final_node])
        final_node = previous[final_node]
        
    route.reverse()
    return(route)
    
if __name__ == '__main__':
    """            a,b,c,d,e,f"""
    M = np.array([[0,1,0,4,0,0],    
                  [1,0,5,7,3,6],
                  [0,5,0,0,0,9],
                  [4,7,0,0,8,0],
                  [0,3,0,8,0,2],
                  [0,6,9,0,2,0]])

    Mn = np.array([[0,580,2000],
                   [0,0,220],
                   [0,0,0]])
    G = nx.DiGraph(Mn)
    cycle = 0
    
    while cycle is 0:
        print(G.nodes())
        source = int(input("Nodo de inicio: "))
        goal = int(input("Nodo final: "))
        distance, route = Dijkstra(G, source, goal)#G: Grafo, Source nodo de inicio, Goal: nodo final
        print("La distancia es {} y la ruta es {}".format(distance, route))
        cycle = int(input("0 para continuar, de lo contrario presione otra tecla: "))

        

