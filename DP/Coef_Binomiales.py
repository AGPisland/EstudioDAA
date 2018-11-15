'''
Calculo de los coeficientes binomiales.
Diseño de un algoritmo con tiempo de complejidad O(nk)
basado con la idea del triangulo de pascal                              
                    0  1  2  3   ...      k-1          k
                0  [1                                     ],
                1  [1  1                                  ],
                2  [1  2  1                               ],
                3  [1  3  3  1                            ],
                4  [1  4  6  4  1                         ],
                5  [1  5  10 10 5  1                      ],
                6  [1  6  15 20 15 6  1                   ],
                .. [.. .. .. ..                           ],
               n-1 [                  C(n-1,k-1)+ C(n-1,k)],
                n  [                                C(n,k)], <--- solucion.

Iremos contruyendo esta tabla por filas de arriba hacia abajo
y de izquierda a derecha mendiante el siguiente algoritmo de 
complejidad polinomica.
PROCEDURE CoefIter(n,k : Cardinal): Cardinal;
    VAR i,j : Cardinal;
          C : Tabla;
BEGIN
FOR i = 0 to n do C[i,0] = 1 end;
FOR i = 1 to n do C[i,1] = i end;
FOR i = 2 to k do C[i,i] = 1 end; 
FOR i = 3 to n do:
    FOR j = 2 to i-1 do:
        if j < = k then:
            C[i,j]= C[i-1, j-1]+C[i-1,j];
        END;
    END;
END;
RETURN C[n,k];
END;

'''
import numpy as np


def CoefBinomiales(n, k):
    Matriz = np.matrix(np.zeros((n, k)))
    for i in range(n):
        Matriz[i, 0] = 1
    for i in range(1, n):
        Matriz[i, 1] = i
    for i in range(2, k):
        Matriz[i, i] = 1
    for i in range(3, n):
        for j in range(2, i):
            if j <= k-1:
                Matriz[i, j] = Matriz[i-1, j-1]+Matriz[i-1, j]
    print(Matriz)
    return Matriz[n-1, k-1]


def Solver():
    Welc = 'PROGRAMA QUE CALCULA EL VALOR DE UN BINOMIO'
    print(Welc)
    n = int(input('INGRESE SU VALOR n'))
    k = int(input('INGRESE SU VALOR k'))
    sol = CoefBinomiales(n+1, k+1)
    print('SOLUCION: ', sol)


if __name__ == '__main__':
    cycle = 0
    while cycle == 0:
        Solver()
        cycle = int(input('OTRO MAS??.... True: 0 .'))
    print('BYEE..:).')
