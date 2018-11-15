import numpy as np 


def Reinas(k):
    #encuentra una manera de disponer la n reinas
    global X, n, exito
    if k>n-1:
        X[k]=-1
        #print('backtrac with limiting')
        return 
    X[k]=-1
    while True:
        X[k]=X[k]+1 #selecciona una nueva opcion.
       # print(X,k)
        if Valido(k): # prueba de fracaso
            if k<n-1:
        #        print('True ',k,'<',n-1)
                Reinas(k+1) #llamada recursiva
            else:
       #         print('Falso ',k,'<',n-1)
                exito=True
        if exito:
            break
        if X[k]==n-1:
            X[k]=-1
      #      print('BackTrack!')
            break
    return 

def Valido(k):
    global X
    #comprueba si el vector solucion X construido hasta el paso k es k-prometedor, es decir, si
    # la reina puede situarse en la columna k
    for i in range(k):
        if X[i]==X[k] or ValAbs(X[i],X[k]) == ValAbs(i,k) :
     #       print('false with is equal or it is diagonal')
            return False
    #print('True why it not is equal and not diagonal')
    return True

def ValAbs(x,y):
    if x>y:
        return x-y
    else:
        return y-x

n=8
X=np.full(n,-1)
exito=False
Reinas(0)
if exito:
    print('Solucion encontrada')
print(X)
Tablero=np.full((n,n),'0')
for i in range(n):
    Tablero[i,X[i]]='R'
print(Tablero)