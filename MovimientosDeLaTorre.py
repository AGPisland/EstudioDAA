def movimientoCaballo(bol1,i,j,Sector):
    const=2
    const2=1
    if bol1:
        if CotasTableAjedrez(i+1,j+2):
            if i+1,j+2 not in Sector:
                Sector.append(i+1,j+2)
                movimientoCaballo(True,i+1,j+2,Sector)
        if CotasTableAjedrez(i+2,j+1):
            if i+2,j+1 not in Sector:
                movimientoCaballo(True,i+1,j+2)
        return True
    else:
        return False
def CotasTableAjedrez(i,j):
    if i < 1 or i > 8:
        return False
    if j < 1 or j>8:
        return False
    return i,j,True
if __name__ is '__main__':
    Sectores=[]
    i=1
    j=2
    movimientoCaballo(True,i,j)





"""
Direcciones del caballo
desde su posicion resta a uno o a dos a la izquierda tambien 
hacia la derecha, luego 1 ssi fueron 2 mov anteriores o 2 si fue 1, 
si no 2 mov hacia la derecha de identidad distancia del movimiento 
hacia la izquierda, si no , 4 movimientos horizontales con la misma 
cantidad de 8 movimientos totales.

8[T,C,A,R,K,A,C,T],
7[P,P,P,P,P,P,P,P],
6[.,.,.,.,.,.,.,.],
5[.,.,.,.,.,.,.,.],
4[.,.,.,.,.,.,.,.],
3[.,.,.,.,.,.,.,.],
2[p,p,p,p,p,p,p,p],
1[t,c,a,k,r,a,c,t].
  / / / / / / / /
 [1,2,3,4,5,6,7,8],
"""