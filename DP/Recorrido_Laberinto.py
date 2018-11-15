import numpy as np
Laberinto = np.array([[0, 2, 0, 0, 0, 0, 0, 0, 0],
                      [0, 2, 0, 2, 0, 2, 0, 0, 0],
                      [3, 0, 0, 2, 0, 2, 3, 0, 0],
                      [0, 2, 0, 2, 0, 0, 2, 2, 0],
                      [3, 0, 0, 2, 2, 3, 2, 2, 0],
                      [0, 2, 0, 2, 2, 0, 0, 3, 3],
                      [3, 0, 0, 0, 2, 2, 2, 0, 2],
                      [0, 2, 3, 0, 3, 3, 3, 0, 0],
                      [2, 3, 0, 3, 3, 0, 0, 0, 0]])
Lista_De_Rutas_Factibles=[]

def AdquirirRuta():
    global Lista_De_Rutas_Factibles
    listaux=[]
    for i in range(n):
        for j in range(m):
            if Laberinto[i,j] == -1:
                listaux.append((i,j))
    print('bingoo', listaux)
    Lista_De_Rutas_Factibles.append(listaux)
                
def Solver(i, j):
    global Laberinto

    # RESULTADO OBTENIDO
    if i == n-1 and j == m-1:
        #hemos llegado a una solucion, pero quiero tener todas las soluciones posibles.
        Laberinto[i, j] = -1
        AdquirirRuta()
        Laberinto[i, j] = 0
        return []
        #return [(i, j)]

    # RUTA NO FACTIBLE
    if Laberinto[i, j] == 2:
        return []

    # DECLARACION DE RECORRIDO
    Laberinto[i, j] = -1

    # COMPROBACION DE RUTA HACIA LA DERECHA.
    if j+1 < m:
        if Laberinto[i, j+1] == 0:
            Ruta = Solver(i, j+1)
            if Ruta != []:
                return [(i, j)]+Ruta
            else:
                Laberinto[i, j] = 0
    # COMPROBACION DE RUTA HACIA LA izquierda.


    # COMPROBACION DE RUTA HACIA ABAJO
    if i+1 < n:
        if Laberinto[i+1, j] == 0:
            Ruta = Solver(i+1, j)
            if Ruta != []:
                return [(i, j)]+Ruta
            else:
                Laberinto[i, j] = 0

    if 0 < j-1:
        if Laberinto[i, j-1] == 0:
            Ruta = Solver(i, j-1)
            if Ruta != []:
                return [(i, j)]+Ruta
            else:
                Laberinto[i, j] = 0

    # CAMBIO EN EL LABERINTO INDICANDO CAMINO YA RECORRIDO Y NO FACTIBLE.

    Laberinto[i, j] = 0
    return []


def Solver2():
    global Laberinto
    ListaDeTesoros=[]
    for i in range(n):
        for j in range(m):
            # si en la coordenada encontramos un tesoro lo agregamos a la lista
            if Laberinto[i,j] == 3:
                ListaDeTesoros.append((i,j))
                Laberinto[i,j] = 0
    print(ListaDeTesoros)
    
m=n=len(Laberinto) # fin laberinto
print(n,m)
Solver2()
print(Laberinto)
X=Solver(0,4)
print(Lista_De_Rutas_Factibles)
print(Laberinto)
