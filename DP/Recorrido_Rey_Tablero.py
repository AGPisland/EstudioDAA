import numpy as np 
def Rey(k,x,y,exito):
    global mov_x, mov_y, tablero, n
    #busca una solucion, si la hay. K indica la etapa, (x,y) las coordenadas de la casilla en donde
    # se encuentra el rey
    orden=-1 #recorre cada uno de los 8 movimiento
    u,v=0,0 # indican la casilla destino desde x,y
    print(tablero)
    while True:
        if exito:
            break
        orden=orden+1
        u=x+mov_x[orden]
        v=y+mov_y[orden]
        if 0<=u and u<=n-1 and 0<=v and v<=n-1:
            if tablero[u,v]==0:
                tablero[u,v]=k
                if k < n*n:
                    Rey(k+1,u,v,exito)
                    if not exito:
                        tablero[u,v]=0
                else:
                    exito=True
                    break
        if exito:
            break
        if orden == 7:
            break

        
            

exito=False
mov_x=[0,-1,-1,-1, 0, 1,1,1]
mov_y=[1, 1, 0,-1,-1,-1,0,1]
n=4
tablero=np.full((n,n),0)
tablero[0,0]=1
Rey(2,0,0,exito)
print(tablero)