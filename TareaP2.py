'''
    Programa que resulve el recorrido de un laberinto.
    El laberinto se compone de una matriz de enteros
    donde son valido solamente el numero 1 y 0.
    El 1 representa una ruta factible y el 0 representa
    una ruta no factible.
    Solucion problema 2 de la tarea de DAA.

    Autor: Alonso Gajardo
    Ultima modificacion: 11/06/18
'''
import numpy as np  # AYUDA PARA TRABAJAR CON MATRIZ DE FORMA MAS COMODA.

'''
                      i          m
                     j  0  1  2  3
                      0[1, 1, 1, 1]
                      1[0, 0, 1, 0]
                      2[0, 0, 1, 0]
                     n3[1, 1, 0, 0]
'''


def Solver(i, j):
    '''
    n la ultima cordenada de i
    m ....................de j
    '''
    # RESULTADO OBTENIDO
    if i == n and j == m:
        return [(i, j)]

    # RUTA NO FACTIBLE
    if Laberinto[i, j] == 0:
        return []

    # DECLARACION DE RECORRIDO
    Laberinto[i, j] = -1

    # COMPROBACION DE RUTA HACIA LA DERECHA.
    if j+1 <= m:
        if Laberinto[i, j+1] == 1:
            Ruta = Solver(i, j+1)
            if Ruta != []:
                return [(i, j)]+Ruta
    # COMPROBACION DE RUTA HACIA ABAJO
    if i+1 <= n:
        if Laberinto[i+1, j] == 1:
            Ruta = Solver(i+1, j)
            if Ruta != []:
                return [(i, j)]+Ruta
    # CAMBIO EN EL LABERINTO INDICANDO CAMINO YA RECORRIDO Y NO FACTIBLE.
    return []


def Print(Laberinto):
    for i in range(n+1):
        print(Laberinto[i, :])
    return


def solMhB():
    Welc = ("+-----------------ALONSO GAJARDO. DAA.>+---PrimerSemestre2018----+\n"
            "|SOLUCION DEL PROBLEMA DE LABERINTO INGRESE EL TAMAÑO DEL TABLERO|\n"
            "|1 REPRESENTA RUTA FACTIBLE, 0 REPRESENTA MURALLA EN EL TABLERO  |\n"
            "|validacion de ingresos..                              y 5:exit. |\n"
            "+----------------------------------------------------------------+\n")
    print(Welc)

    '''Declaracion de variables globales del programa.'''
    global n
    n = int(input('Largo n: '))
    global m
    m = int(input('Largo m: '))

    # Validacion:
    if n < 1 or m < 1:
        print('NO!')
        return False

    '''Laberinto como matriz global para ir transformando la ruta en la matriz solucion.'''
    global Laberinto
    Laberinto = np.matrix(np.zeros((n, m)))

    # auxiliares
    iter = 0
    v = []

    # Solicitud de tablero ingreso por filas, validacion de longitud columna.
    while iter != n:
        g = input('Fila:')
        if g is '5':
            return False
        if len(g) == m:
            v.append(g)
            iter = iter+1
        else:
            print('ERROR')

    # Generacion de la matriz laberinto
    for i in range(n):
        u = v[i]
        for j in range(m):
            Laberinto[i, j] = int(u[j])

    # Requerimiento funcion solver.
    n = n-1  # indice final de eje fila
    m = m-1  # indice final de eje columna

    Print(Laberinto)  # Funcion que imprime la matriz
    # Funcion solucion matriz laberinto, retorna una lista de caminos.
    sol = Solver(0, 0)
    Laberinto = np.matrix(np.zeros((n+1, m+1)))
    for x in sol:
        Laberinto[x] = 1
    print('SOLUCION: ')
    Print(Laberinto)  # Imprime la matriz solucion.
    return


if __name__ == '__main__':
    cycle = 0
    while cycle == 0:
        solMhB()
        cycle = int(input('OTRO MAS??.... True: 0 .'))
    print('BYEE..:).')
