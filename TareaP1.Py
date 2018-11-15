'''
    Programa que resuelve el calculo de una ruta maxima en un grafo unidireccional
    utilizando el algoritmo de dijkstra modificado. Tambien resuelve el problema de
    seleccion minima de cantidades que ponderan un numero mayor entero, utilizando
    programacion dinamica el algortimo de "el problema del cambio". Sacado del libro
    de "tecnias del diseño de algoritmos."
    
    Autor: Alonso Gajardo
    Ultima modificacion: 12/06/18
'''
'''
ANALISIS:
SOLUCION PROBLEMA DE PROGRAMACION DINAMICA:
1- ECUACION DE RECURRENCIA DE DECISIONES OPTIMAS:
EL PROBLEMA DEL CAMBIO...
SEA C UN VECTOR DE LARGO L, C VA CONTANDO LA CANTIDAD DE MONEDAS QUE SE NECESITAN 
PARA TENER TAL OPTIMO. DADO Ti = Moneda en el indice i y j es la cantidad que se desea obtener y va de uno en uno.
SOLUCION:
sea n el numero de tipos de monedas distintos, L la cantidad a conseguir y T[1..n] 
un vector con el valor de cada tipo de moneda del sistema. Supondremos que disponemos
de una cantidad inagotable de monedas de cada tipo.
Llamaremos C(i,j) para (1 <= i <= n) y (1 <= j <= L) al numero minimo de monedas para obtener
la cantidad j restringiendose a los tipos T[1], T[2], ... T[n]. Si no se puede conseguir dicha
cantidad entonces C(i,j)=inf. En primer lugar hemos de encontrar una expresion recursiva de
C(i,j). Para ello observamos que en cada paso existen dos opciones:
    1. No incluir ninguna moneda del tipo T(i). Esto supone que el valor de C(i,j) va a coincidir
       con el de C(i-j,j), y por tanto C(i,j)=C(i-1,j)
    2. Si incluir. Pero entonces, al incluir la moneda del tipo T(i), el numero de monedas global
       coincide con el numero optimo de monedas para obtener una cantidad (j-T(i)) mas esta moneda T(i)
       que se incluye, es decir podemos expresar C(i,j) es este caso como C(i,j)=1+C(i,j-T(i))..
El calculo de C(i,j) optimo tomara la solucion mas favorable, es decir, el menor valor de ambas opciones.
Con esto, la relacion en recurrencia queda definida de la forma anterior.
SEA LA SIGUIENTE ECUACION DE RECURRENCIA.
         | inf                                  si i = 1 y 1 <= j < T(i)
         | 0                                    si j = 0
  C(i,j)=| 1+C(i,j-T(i))                        si i = 1 y j >= T(i)
         | C(i-1,j)                             si i > 1 y j < T(i)
         | MIN{ C(i-1, j), 1 + C(i,j-T(i))}     en otro caso
'''

import networkx as nx
import numpy as np
from heapq import heappush, heappop


def Procedencia(P, Cambio, L, n, T):
    '''ESTA FUNCION RECIBE DOS MATRICES DE COLUMNA L+1 Y FILAS n.
       LAS COLUMNAS SE ENUMERAN POR EL TAMAÑO A COMPONER TOTAL
       POR TANTO L=TOTAL.
       LA MATRIZ P ES BOOLEANA INDICANDO QUE INDICE DE FILA PUEDE
       COMOPONER EL VALOR j QUE SE MUEVE DESDE 0 HASTA L.
       LA MATRIZ CAMBIO GUARDA EL CONTADOR DE INDICES i NECESARIOS 
       PARA PODER COMPONER EL VALOR L.
       LA SOLUCION SE ENCUENTRA EN Cambio[L].
       n: TAMAÑO DEL ARREGLO DE OPCIONES T Y FILA DE LA MATRIZ P Y CAMBIO.
       T: VECTOR QUE CONTIENE LAS OPCIONES DE LAS CUALES SE DEBE COMPONER j:[0..L]
       '''
    for i in range(n):
        P[i, 0] = False
        Cambio[i, 0] = 0
    '''PARA CADA MONEDA i COMPROBAMOS SI PUEDE SER COMPUESTA PARA j'''
    for i in range(n):
        for j in range(1, L+1):
            '''LA PRIMERA OPCION i==0 LA PRIMERA FILA'''
            ''''''
            if i == 0 and j < T[i]:
                Cambio[i, j] = float('inf')
                P[i, j] = False
            elif i == 0:
                Cambio[i, j] = 1+Cambio[i, j-T[i]]
                P[i, j] = True
            elif j < T[i]:
                Cambio[i, j] = Cambio[i-1, j]
                P[i, j] = False
            else:
                Cambio[i, j] = min(Cambio[i-1, j], 1+Cambio[i, j-T[i]])
                P[i, j] = (Cambio[i, j] != Cambio[i-1, j])


def Solucion(P, Cambio, L, n, T, monedas):
    '''RECORREMOS LA MATRIZ P Y CAMBIO DE FORMAS DESCENDENTE Y COMPROBAMOS SI COMPONE t[I] EL VALOR
        TRUE DE LA MATRIZ P.
    '''
    i, j = n-1, L
    for ind in range(n):
        monedas[ind] = 0
    while i > 0 and j > 0:
        if P[i, j] == False:
            i = i-1
        else:
            monedas[i] = monedas[i]+1
            j = j-T[i]
    if i == 0:
        monedas[1] = Cambio[i, j]+monedas[1]
    return monedas


def Dijkstra(G, initial_node, final_node):
    distance = {initial_node: 0}
    previous = {}
    nodes = set(G.nodes())
    heap = []
    min = 0
    current_distance = 0

    for node in nodes:
        if node is not initial_node:
            '''CAMBIAMOS ESTA PARTE DE LA FUNCION DJKSTRA PARA QUE CALCULE UNA RUTA MAXIMA.'''
            distance[node] = 0  # float('inf')
        heappush(heap, node)

    while heap:
        min = heappop(heap)
        for node in nodes:
            if G.has_edge(min, node) and G[min][node]['weight'] != 0:
                current_distance = distance[min] + G[min][node]['weight']
                '''CAMBIAMOS EL SENTIDO DEL SIMBOLO MENOR PARA QUE FUNCIONE LA BUSQUEDA DE RUTA MAX.'''
                if current_distance > distance[node]:
                    distance[node] = current_distance
                    previous[node] = min
                    heappush(heap, node)
    return distance[final_node]  # ,Path(previous, initial_node, final_node)


'''
FUNCION QUE RETORNA LA RUTA DE DIJKSTRA, NO ES NECESARIO USARLA EN ESTE CASO, YA QUE IMPORTA MAS EL
VALOR DEL MAXIMO DE EL COMO RECORRE EL GRAFO.
def Path(previous, initial_node, final_node):
    route = [final_node]
    while final_node is not initial_node:
        route.append(previous[final_node])
        final_node = previous[final_node]
    route.reverse()
    return(route)
'''


def Print(Tabla, n):
    for i in range(n):
        print(Tabla[i, :])
    return


def Solver():
    Welc = ("+-----------------ALONSO GAJARDO. DAA.>+---PrimerSemestre2018----+\n"
            "|SE SOLUCIONAN LOS SIGUIENTES PROBLEMAS:                         |\n"
            "|  1- BUSQUEDA DE UNA RUTA MAXIMA EN UN GRAFO UNIDIRECCIONAL.    |\n"
            "|  2- ENCONTRAR UNA COMPOSICION MINIMA DE  CANTIDADES QUE PUEDEN |\n"
            "|     PONDERAR UN VALOR ENTERO POSITIVO.                         |\n"
            "|LAS SOLUCION SE ESCRIBE EN BASE A LAS SIGUIENTES MATERIAS:      |\n"
            "|  1- MODIFICACION DEL ALGORITMO DIJKSTRA PARA BUSCAR EL         |\n"
            "|     MAXIMO COSTO DE UNA RUTA DE ORIGEN A DESTINO.              |\n"
            "|  2- PROGRAMACION DINAMICA ALGORITMO DEL PROBLEMA CAMBIO   DE   |\n"
            "|     MONEDAS.                                                   |\n"
            "|PRIMERO SE INGRESA LA MATRIZ CUADRADA DE ABYACENCIA UNIDIRECCIO-|\n"
            "|NAL, SE ASUME EL ORIGEN EN 0,0 Y DESTINO EN n-1, n-1. CON n     |\n"
            "|TAMAÑO DE LA MATRIZ CUADRADA.                                   |\n"
            "|LUEGO SE SOLICITA LA CANTIDAD DEL ARREGLO QUE SE DESEA PONDERAR |\n"
            "|USANDO EL ALGORITMO DE PROGRAMACION DINAMICA.                   |\n"
            "|                                                                |\n"
            "|validacion de ingresos..                              y 5:exit. |\n"
            "+----------------------------------------------------------------+\n")
    print(Welc)
    print('INGRESO MATRIZ CUADRADA UNIDIRECCIONAL')
    n = int(input('INGRESE TAMAÑO: '))
    if n < 1:
        print('NO!')
        return False
    Matriz_Abyacencia_UNI = np.matrix(np.zeros((n, n)))
    # auxiliares
    v = []
    for i in range(n):
        iter = 0
        print('FILA: ')
        c = []
        while iter != n:
            aux = int(input('>>'))
            if aux < 0:
                print('ERROR')
            else:
                c.append(aux)
                iter = iter+1
        v.append(c)
        u = v[i]
        for j in range(n):
            Matriz_Abyacencia_UNI[i, j] = u[j]
    Print(Matriz_Abyacencia_UNI, n)

    m = int(input('INGRESE m: '))
    iter = 0
    v = []
    L = 0
    while iter != m:
        inte = int(input('Valor: '))
        if inte <= 1:
            print('ERROR')
        else:
            v.append(inte)
            L = L+inte
            iter = iter+1
    Grafo = nx.DiGraph(Matriz_Abyacencia_UNI)
    Costo = Dijkstra(Grafo, 0, n-1)
    print('SOLUCION DIJKSTRA: Costo: ', Costo)

    L = L + int(Costo)
    '''LA SOLUCION NO FUNCIONA BIEN PARA DOS TIPOS, POR ENDE AUMENTO A 3 EL TAMAÑO Y COLOCO UNA
    OPCION QUE NUNCA PODRA UTILIZAR.'''
    T = [L+2, 700, 400]
    n = len(T)
    i = [0, 1, 2]
    Num = np.zeros(n)
    P = np.matrix(np.zeros((n, int(L+1)), dtype=bool))
    cambio = np.matrix(np.zeros((n, L+1)))
    print('SOLUCION PROBLEMA DEL CAMBIO DE MONEDAS:')
    print('--Sea la cifra a ponderar: ', L)
    print('--Sean las opciones de composicion : ', T[1], ',', T[2])
    print('CALCULANDO::\n')
    Procedencia(P, cambio, L, n, T)
    x = Solucion(P, cambio, L, n, T, Num)
    print('RESULTADO PARA OPTENER: ', L, ' ES LA MINIMA COMPOSICION ENTRE: ')
    for t in range(1, n):
        if T[t] == 700:
            print(int(x[t]), 'u DE POWERADE')
        else:
            print(int(x[t]), 'u DE DORITOS\n')
    print('FIN SOLUCION GLOBAL!')


if __name__ == '__main__':
    cycle = 0
    while cycle == 0:
        Solver()
        cycle = int(input('OTRO MAS??.... True: 0 .'))
    print('BYEE..:).')
