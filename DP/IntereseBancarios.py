'''
5.5 Intereses Bancarios
Dadas n funciones f1, f2,,,,,fn y un entero positivo M, deseamo maximizar la 
funcion f1(x1)+f2(x2)+,,,,+fn(xn) sujeta a la restriccion x1+x2+....xn=M, donde
fi(0)=0 (i=1,2,,,,n), xi son numeros naturales, y todas las funciones son monotonas crecientes,
es decir, x<y, f(x)<f(y). Supongase que los valores de cada funcion se almacenan en un vector.
Este problema tiene una aplicacion real muy interesante, en donde fi representa la funcion
de interes que proporciona el banco i y lo que deseamo es maximizar el interes total al invertir una
cantidad determinanda de dinero M. Los valores xi van a representa la cantidad a invertir en cada
unos de los n bancos.

Solucion:
Sea fi un vector que almacena el interes del banco i (1<i<n) para ina inversion de 1,2,3,,,,M pesetas.
Esto es, fi(j) indicara el interes que ofrece el banco i para j pesetas, con 0<i<n, 0<j<M.
Para poder plantear el problema como una sucesion de decisiones, llamaremos In(M) al interes
maximo al invertir M pesetas en n bancos.

                    In(M)=f1(x1)+f2(x2)+,,,,,,+fn(xn)
que es la funcion a maximizar, sujeta a la restriccion x1+x2+,,,,+xn=M.
Veamos como aplicar el principio de optimo. Si In(M) es el resultado de una secuencia de decisiones
y resulta ser optima para el problema de invertir una cantidad M en n bancos, cualquiera de sus 
subsecuencias de decisiones ha de ser tambien optima y asi la cantidad

                    In-1(M-xn)=f1(x1)+f2(x2)+,,,,+fn-1(xn-1)
Sera tambien optima para el subproblema de invertir (M-xn) pesetas en n-1 bancos. Y por tanto el 
principio de optimo nos lleva a plantear la siguiente relacion de recurrencia:
                           ____________________________________
                          |               
                          |f1(x)                   si n=1
                    In(x)=|                    
                          |Max{In-1(x-t)+fn(t)}    en otro caso
                          |____________________________________

Para resolverla y calcular In(M), vamos a utilizar una matriz I de dimension nxM en donde iremos
almacenando los resultados parciales y asi eliminar la repeticion de los calculos.
El valor de I[i,j] va a representar el interes de j pesetas cuando se dispone de i bancos, por tanto 
la solucion buscada se encontrara en I[n,M].
Para guardar los datos iniciales del problema vamos a utilizar otra matriz F de la misma dimension
y donde F[i,j] representa el interes del banco i para j pesetas.
En consecuencia, para calcular el valor pedido de I[n,M] rellenaremos la tabla por filas, empezando
por los valores iniciales de la ecuacion en recurrencia y segun el siguiente algoritmo.

CONST n=.....;(*NUMERO DE BANCOS A INVERTIR)
      m=.....;(*CANTIDAD A INVERTIR)
TYPE MATRIZ=ARRAY[1..n][0..m] OF CARDINAL;
PROCEDURE Interes(VAR F:MATRIZ; VAR I:MATRIZ): CARDINAL;
    VAR i,j: CARDINAL
BEGIN
    FOR i=1 TO n DO I[i,0]=0 END;
    FOR j=1 TO m DO I[1,j]=F[1,j] END;
    FOR i=2 TO n DO:
        FOR j=1 TO m DO:
            I[i,j]=Max(I,F,i,j)
        END
    END;
    RETURN I[n,m]
END Intereses;

PROCEDURE Max(VAR I,F: MATRIZ; i,j: CARDINAL):CARDINAL;
    VAR max,t:CARDINAL;
BEGIN
    max=I[i-1,j]+F[i,0]
    FOR t=1 TO j DO:
        max=MAX(max, I[i-1, j-1]+F[i,t])
    END;
    RETURN max
END Max

LA COMPLEJIDAD DEL ALGORITMO COMPLETO ES DE ORDEN O(nMxM). PUESTO QUE LA COMPLEJIDAD DE MAX ES O(j) Y SE INVOCA DENTRO
DE DOS BUCLES ANIDADOS QUE SE DESARROLLAN DE 1 HASTA M. ES IMPORTANTE HACER NOTAR EL USO DE PARAMETROS POR REFERENCIA
EN LUGAR DE POR VALOR PARA EVITAR LA COPIA DE LAS MATRICES EN LA PILA DE EJECUCION DEL PROGRAMA.
POR OTRO LADO, LA COMPLEJIDAD ESPACIAL DEL ALGORITMO ES DEL ORDEN O(nM), PUES DE ESTE ORDEN SON LAS DOS MATRICES QUE
SE UTILIZAN PARA ALMACENAR LOS RESULTADOS INTERMEDIOS.
EN ESTE EJEMPLO QUEDA DE MANIFIESTO LA EFECTIVIDAD DEL USO DE ESTRUCTURAS EN LOS ALGORITMOS DE PROGRAMACION DINAMICA PARA
CONSEGUIR OBTENER TIEMPOS DE EJECUCION DE ORDEN POLINOMICO, FRENTE A LOS TIEMPOS EXPONENCIALES DE LOS ALGORITMOS
RECURSIVOS INICIALES.

'''
import numpy as np
                 #1, 2, 3
F = np.array([[0, 0, 0, 0],
              [0, 45, 20, 50],
              [0, 70, 45, 70],
              [0, 90, 75, 80],
              [0, 105, 110, 100],
              [0, 120, 150, 130]])
I = np.matrix(np.zeros((6, 4)))


def Intereses(I, F, n, m):
    for i in range(1, n):
        I[i, 0] = 0
    print(I)
    for j in range(1, m):
        I[1, j] = F[1, j]
    print(I)
    for i in range(2, n):
        for j in range(1, m):
            I[i, j] = Max2(I, F, i, j)
            print(I)
        print(I)
    print(I)
    return I[n-1, m-1]


def Max2(I, F, i, j):
    maxi = I[i-1, j]+F[i, 1]
    for t in range(1,j+1):
        maxi = max(maxi, I[i-1, j-1]+F[i, t])
        print(maxi)
    return maxi
print(Intereses(I,F,6,4))