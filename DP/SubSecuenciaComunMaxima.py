'''
EJERCICIO PARA COMPRENDER LA COMPOSICION MAXIMA DE UNA SUBSECUENCIA DE DOS SECUENCIAS..
LA IDEA PRINCIPAL CONSISTE NO SOLO EN GUARDAR VALORES FINALES SI NO TAMBIEN
GUARDAR VALORES PARCIALES DE COMO SE HA LLEGADO A LA SOLUCION.
ESTA SOLUCION PARCIAL PUEDE SER ALMACENADA EN LA MISMA TABLA DE SOLUCION O
EN OTRA.
DADA UNA SECUENCIA X={x1, x2, ..., xM}, DECIMOS QUE Z={z1, z2, ...., zK} ES UNA
SUBSECUENCIA DE X SI EXISTE UNA SECUENCIA CRECIENTE {i1. i2, ...., ik} DE INDICES
DE X TALES QUE PARA TODO j=1,2,...,k TENEMOS xij=zj.
DADAS DOS SECUENCIAS X E Y, DECIMOS QUE Z ES UNA SUBSECUENCIA COMUN DE X E Y SI
ES SUBSECUENCIA DE X Y SUBSECUENCIA DE Y, DESEAMOS DETERMINAR LA SUBSECUENCIA DE 
LONGITUD MAXIMA COMUN A DOS SECUENCIAS.
SOLUCION:
llamaremos L(i,j) a la longitud de la secuencia comun maxima de la secuencias Xi e Yj
, siendo Xi el i-esimo prefijo de X (esto es Xi={x1,x2,...xi}) e Yj el j-esimo prefijo de Y
(Yj={y1,y2,...,yj}).
Aplicando el principio de optimo podemos plantear la solucion como una sucesion de decisiones en las que en cada
paso determinaremos si un caracter formar o no parte de scm.
Escogiendo una estrategia hacia atras, es decir, comenzando por los ultimos caracteres de las dos secuencias X e Y,
la solucion viene dada por la siguiente relacion en recurrencia:
        _______________________________________________
       |
       |0                       si i=0 o j=0
L(i,j)=|L(i-1, j-1)+1           si i!=0, j!=0 y xi=yj
       |Max{L(i,j-1),L(i-1,j)}  si i!=0, j!=0 y xi!=yj
       |_______________________________________________
       
La solucion recursiva resulta ser de orden exponencial, y por tanto DP va a construir una tabla con los valores L(i,j)
para evitar la repeticion de calculos. Para ilustrar la construccion de la tabla supondremos que X e Y son las secuencias
de valores:
    X={1 0 0 1 0 1 0 1}  len(8)
    Y={0 1 0 1 1 0 1 1 0}  len(9)

          0    1     2     3     4     5     6     7     8

               1     0     0     1     0     1     0     1

0       | 0 |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
        |   |     |     |     |     |     |     |     |     |
1    0  | 0 |  0  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |
        |   | sup | dia | dia | izq | dia | izq | dia | izq |
2    1  | 0 |  1  |  1  |  1  |  2  |  2  |  2  |  2  |  2  |
        |   | dia | sup | sup | dia | izq | dia | izq | dia |
3    0  | 0 |  1  |  2  |  2  |  2  |  3  |  3  |  3  |  3  |
        |   |     |     |     |     |     |     |     |     |
4    1  | 0 |  1  |  2  |  2  |  3  |  3  |  4  |  4  |  4  |
        |   |     |     |     |     |     |     |     |     |
5    1  | 0 |  1  |  2  |  2  |  3  |  3  |  4  |  4  |  5  |
        |   |     |     |     |     |     |     |     |     |
6    0  | 0 |  1  |  2  |  3  |  3  |  4  |  4  |  5  |  5  |
        |   |     |     |     |     |     |     |     |     |
7    1  | 0 |  1  |  2  |  3  |  4  |  4  |  5  |  5  |  6  |
        |   |     |     |     |     |     |     |     |     |
8    1  | 0 |  1  |  2  |  3  |  4  |  4  |  5  |  5  |  6  |
        |   |     |     |     |     |     |     |     |     |
9    0  | 0 |  1  |  2  |  3  |  4  |  5  |  5  |  6  |  6  |
        |   |     |     |     |     |     |     |     |     |

Esta tabla se va construyendo por filas y rellenando de izquierda a derecha. Como podemos
ver en cada L[i,j] hay dos datos: uno el que corresponde a la longitud de cada subsecuencia, y otro
necesario para la construccion de la subsecuencia optima.
la solucion a la subsecuancia comun maxima de las secuencias X eY se encuentra en el extremo inferior
 y por tanto su longitud es 6.
El algoritmo para construir la tabla tiene una complejidad de orden O(nm), siendo n y m las longitudes de las
secuencias X e Y.
CONST N=....; *LONGITUD MAXIMA DE UNA SECUENCIA*
TYPE    SECUENCIA=ARRAY[1...N] OF CARDINAL
        PARES= RECORD numero : CARDINAL; procedencia : CHAR; END;
        TABLA= ARRAY[0..N][0..N] OF PARES;

PROCEDURE SubSeqMax(VAR X,Y:SECUENCIA; n,m:CARDINAL; VAR L:TABLA);
        VAR i,j: CARDINAL;
BEGIN
        FOR i = 0 to m do:
                L[i,0].numero=0;
        END;
        FOR j = 0 to n do:
                L[0,j].numero=0;
        END;
        FOR i = 1 to m do:
                FOR j = 1 to n do:
                        if Y[i] = X[j] then:
                                L[i,j].numero=L[i-1,j-1].numero+1;
                                L[i,j].procedencia='diagonal';
                        elif L[i-1,j].numero >= L[i,j-1].numero then:
                                L[i,j].numero=L[i-1,j].numero;
                                L[i,j].procedencia='superior';
                        else:
                                L[i,j].numero=L[i,j-1].numero;
                                L[i,j].procedencia='izquierda';
                        END
                END
        END
END SubSeqMax

PARA ENCONTRAR CUAL ES ESA SUBSECUENCIA OPTIMA HACEMOS USO DE LA INFORMACION 
CONTENIDA EN EL CAMPO PRECEDENCIA DE LA TABLA L, SABIEN QUE 'I'(POR IZQUIERDA)
EL ALGORTIMO QUE RECORRE LA TABLA CONSTRUYENDO LA SOLUCION A PARTIR DE ESTA INFORMACION Y DE LA 
SECUENCIA Y ES EL QUE SIGUE:

PROCEDURE Escribir(VAR L:TABLA; VAR Y: SECUENCIA; i,j :CARDINAL;
                   VAR sol: SECUENCIA; VAR l:CARDINAL;)
                #sol es la secuencia solucion, l su longitud
                # i es la longitud de la secuencia Y, j es la 
                #longitud de la secuencia X
BEGIN
    if (i=0) or (j=0) then return end;
    if L[i,j].procendencia='D' then:
        Escribir(L,Y,i-1,j-1,sol,l);
        sol[l]=Y[i]
        l=l+1
    elsif L[i,j].procedencia='S' then:
        Escribir(L,Y,i-1,j,sol,l)
    else:
        Escribir(L,Y,i,j-1,sol,l)
    END
END ESCRIBIR

'''


def EstructuraDeDatos(X, Y):
    matrix = []
    Fila = []
    for row in range(Y):
        for colum in range(X):
            Fila.append((0, 'null'))
        matrix.append(Fila)
        Fila = []
    #PRINT(matrix, Y)
    return matrix


def PRINT(L, y):
    for i in range(y):
        print(L[i], '\n')


def SubSecuenciaMax(X, Y):
    L = EstructuraDeDatos(len(X), len(Y))
    for i in range(len(Y)):
        L[i][0] = (0, ' ok ')
    for j in range(len(X)):
        L[0][j] = (0, ' ok ')
    # PRINT(L,len(Y))

    for i in range(1, len(Y)):
        for j in range(1, len(X)):
            #print(L[i-1][j][0],'>=',L[i][j-1][0], ' indices ',X[j],'==',Y[i])
            if X[j] == Y[i]:
                L[i][j] = L[i-1][j-1][0]+1, 'Diag'

            elif L[i-1][j][0] >= L[i][j-1][0]:
                L[i][j] = L[i-1][j][0], 'Supe'

            else:
                L[i][j] = L[i][j-1][0], 'Izqu'
    PRINT(L, len(Y))
    return L


def Escribir(L, Y, i, j, sol):
    if i is 0 or j is 0:
        return
    if L[i][j][1] is 'Diag':
        Escribir(L, Y, i-1, j-1, sol)
        sol.append(Y[i])
    elif L[i][j][1] is 'Supe':
        Escribir(L, Y, i-1, j, sol)
    else:
        Escribir(L, Y, i, j-1, sol)


def Solver():
    Y = ['2', 'B', 'A', 'N', 'A', 'N', 'A']
    X = ['2', 'A', 'T', 'A', 'N', 'A']
    L = SubSecuenciaMax(X, Y)
    sol = []
    Escribir(L, Y, len(Y)-1, len(X)-1, sol)
    print(sol)


if __name__ is '__main__':
    Solver()
