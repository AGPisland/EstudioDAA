import numpy as np
import Networkxxx as xxx


def Definidor_Grafos(MAbyacencia):
    """funcion que retorna G[V,E], retorna V=vertices, E= de edges de un grafo,
    ponderado como una matriz de abyacencia"""
    n = len(MAbyacencia)
    Edges = set()
    Vertex = set()
    for i in range(0, n):
        Vertex.add(i+1)
        for j in range(i+1, n):
            if MAbyacencia[i, j] != 0:
                Edges.add((i+1, j+1))

    return Vertex, Edges

def Definidor_matriz_Abyacencia(Edges, Matriz):
    """ Suponemos que Edges es un vector de nX2 dimensiones"""
    M = Matriz
    for i in range(1,len(M)+1):
        for j in range(1,len(M)+1):
            if [i,j] in Edges:
                pass
            else:
                M[i-1, j-1] = 0
    return M

def ListaSet(SETT):
    lista = []
    for i in range(len(SETT)):
        lista.append(SETT.pop())
    for i in range(len(lista)):
        SETT.add(lista[i])
    return lista

def min_grafo(Matriz, Edges):
    lista = list(Edges)
    min1 = 10000
    k, l = 0, 0
    for i in range(len(lista)):
        Costo = Matriz[lista[i][0]-1, lista[i][1]-1]
        if Costo < min1:
            min1, k, l = Costo, lista[i][0], lista[i][1]
    return k, l

def Let_J(M, Near):
    minc = 1000
    for j in range(len(Near)):
        if Near[j] != -1:
            if M[j, Near[j]] != 0:
                if M[j, Near[j]] < minc:
                    minc = M[j, Near[j]]
                    l = j+1
    return l

Edges = set([
    (1, 2),
    (1, 6),
    (2, 3),
    (2, 7),
    (3, 4),
    (4, 5),
    (4, 7),
    (5, 6),
    (5, 7),
])
MatrizCosto = np.array([
    [0, 28, 0, 0, 0, 10, 0],
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0],
    [0, 0, 12, 0, 22, 0, 18],
    [0, 0, 0, 22, 0, 25, 24],
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 24, 0, 0],
])

def prim(E, M, n):
    k, l = min_grafo(M, E)  # =1,6
    """Calculamos la ruta mas corta de las lineas de conexion."""
    k, l = k-1, l-1  # =0,5
    """Guardamos tal ruta como un numero de cordenadas, l=5, k=0, talque que k=1,l=6 la primera ruta"""
    costMin = M[k, l]
    T, Near = [], []
    T.append([k+1, l+1])
    for i in range(n):
        """Comparamos costos tal que desde la arista l exista otra linea de costo menor"""
        """esto quiere decir que en la matriz de abyacencia si, no hay un camino no debe ser considerada"""
        costo1 = 100000 if M[i, l] == 0 else M[i, l]
        costo2 = 100000 if M[i, k] == 0 else M[i, k]
        """suponemos que si no hay un camino hacia una arista esta debe tener valor de infinito."""
        if costo1 < costo2:
            Near.append(l)
        else:
            Near.append(k)
        """near= [0,0,0,0,5,0,0]
                 [0,1,2,3,4,5,6]
                 quiere decir que, desde 
        """
        """Creamos un arreglo near con el valor de arista en el cual el algoritmo debe comprobar costos."""
    Near[k] = Near[l] = -1
    for i in range(1, n-1):
        j = Let_J(M, Near)  # problemas......
        T.append([Near[j-1]+1, j])
        costMin = costMin+M[j-1, Near[j-1]]
        Near[j-1] = -1
        for u in range(n):
            costo1 = 10000000 if M[k, Near[u]] == 0 else M[k, Near[u]]
            costo2 = 10000000 if M[u, j-1] == 0 else M[u, j-1]
            if Near[u] != -1 and (costo1 > costo2):
                Near[u] = j-1
    return T

T=prim(Edges, MatrizCosto, 7)
xxx.Dibujar_Grafo(MatrizCosto)
MatrizNueva=Definidor_matriz_Abyacencia(T,MatrizCosto)
xxx.Dibujar_Grafo(MatrizNueva)

"""
pseudocode:
E is the set of edges in G, cost[1:n, 1:n] is the cost abjacency matrix of an n vertex
graph such that cost[i,j] is either a positiveNear[j-1]+1 number or infinity if no edge exist.
"""
