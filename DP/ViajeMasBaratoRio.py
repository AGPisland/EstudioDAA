'''
5.6 El viaje mas barato por rio.
Sobre un rio x hay n embarcaderos. En cada uno de ellos se puede alquilar un bote que permite ir 
a cualquier otro embarcadero rio abajo (es imposible ir rio arriba). Existe una tabla de tarifas
que indica el coste del viaje del embarcadero i al j para cualquier embarcadero de partida i y 
cualquier embarcadero de llegada j mas abajo en el rio i<j. Puede suceder que un viaje de i a j
sea mas caro que una sucesion de viajes mas cortos, en cuyo caso se tomaria un primer bote hasta un 
embarcadero k y un segundo bote para continuar a partir de k. No hay coste adicional por cambiar de 
bote. 
Nuestro problema consiste en diseñar un algoritmo eficiente que determine el coste minimo
para cada par de puntos  i,j i=<j y determinar, en funcion de n, el tiempo empleado por el algoritmo.
Solucion:
Llamaremos T[i,j] a la tarifa para ir del embarcadero i al j (directo). Estos valores se almacenaran
en una matriz triangular superior de orden n, siendo n el numero de embarcaderos. El problema puede
resolverse mediante programacion dinamica ya que para calcular el coste optimo para ir del 
embarcadero i al j podemos hacerlo de forma recurrente, suponiendo que la primera parada la realizamos
en un embarcadero intermedio k (i<k<j):

                            C(i,j)=T(i,k)+C(k,j)
        
En esta ecuacion se contempla el viaje directo, que corresponde al caso en el que k coincide con j.
Esta ecuacion verifica tambien que la solucion buscada C(i,j) satisface el principio del optimo,
pues el coste C(k,j), que forma parte de la solucion, ha de ser, a su vez optimo. Podemos plantear
entonces la siguiente expresion de la solucion:
                           ____________________________________
                          |               
                          |0                       si i=j
                   C(i,j)=|                    
                          |Min{T(i,k)+C(k,j)}      si i<j
                          |____________________________________

La idea de esta segunda expresion surge al observar que en cualquiera de los trayectos siempre
existe un primer salto inicial optimo.
Para resolverla segun tecnica de programacion dinamica, hace falta utilizar una estructura 
para almacenar resultados intermedios y evitar la repeticion de los calculos. La estructura
que usaremos es una matriz triangular de costes C[i,j], que iremos rellenando por diagonales
mediante el procedimiento que hermos denominado Costes. La solucion al problema es la propia 
tabla, y sus valores C[i,j] indican el coste optimo para ir de embarcadero i al j.

CONST MAXEMBARCADEROS =....;
TYPE MATRIZ=ARRAY[1..MAXEMBARCADEROS][1..MAXEMBARCADEROS] OF CARDINAL;

PROCEDURE Costes(VAR C:MATRIZ; n:CARDINAL);
    VAR i,diagonal:CARDINAL;
BEGIN
    FOR i=1 TO n DO C[i,i]=0 END; *condiciones iniciales*
    FOR diagonal=1 TO n-1 DO:
        FOR i=1 TO n-diagonal DO:
            C[i,i+diagonal]=Min(C,i,i+diagonal)
        END
    END
END Costes

PROCEDURE Min(VAR C:MATRIZ; i,j:CARDINAL):CARDINAL;
    VAR k,min: CARDINAL;
BEGIN
    min=MAX(CARDINAL)
    FOR k=i+1 TO j DO:
        min=Min2(min,T[i,k]+C[k,j])
    END
    RETURN MIN
END
La funcion min2 es la que calcula el minimo de dos numeros naturales. Es importante observar que esta funcion,
por la forma en que se va rellenando la matriz C, solo hace uso de los elementos calculados hasta el momento.
La complejidad del algoritmo es de orden O(n3), pues esta compuesto por dos bucles anidados de tamaño n, que 
contienen la llamada a una funcion de orde O(n), la que calcula el minimo.
'''
import numpy as np
n = 6
Tarifas = np.array([[0, 5, 2, 10, 3, 7],
                    [0, 0, 3, 1, 2, 6],
                    [0, 0, 0, 1, 3, 4],
                    [0, 0, 0, 0, 2, 2],
                    [0, 0, 0, 0, 0, 7],
                    [0, 0, 0, 0, 0, 0]])
C = np.matrix(np.zeros((n, n)))

def Costes(T, C, n):
    for diagonal in range(1,n):
        for i in range(n-diagonal):
            C[i, i+diagonal] = Min(T, C, i, i+diagonal)
    return C


def Min(T, C, i, j):
    min2 = 999
    for k in range(i+1, j+1):
        min2 = min(min2, T[i, k]+C[k, j])
    return int(min2)

print(Tarifas)
print(Costes(Tarifas, C, n))
