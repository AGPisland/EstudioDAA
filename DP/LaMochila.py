'''
5.16 La Mochila (0,1)
En el apartado 4.7 se planteo el problema de la mochile (0,1), que consistia en decidir de entre n objetos de pesos p1,p2,....,pn y
beneficios b1, b2,....,bn, cuales hay que incluir en una mochile de capacidad M sin superar dicha capacidad y de forma que 
maximice la suma de los beneficios de los elementos escogidos. Los algoritmos avidos planteados entonces no conseguian resolver
el problema. Nos cuestionamos aqui si este problema admite una solucion mediante DP.
Solucion:
Para encontrar un algoritmo de DP que lo resuelva, primero hemos de plantear el problema como una secuencia de deciciones que
verifique el principio del optimo. De aqui seremos capaces de deducir una expresion recursiva de la solucion. Por ultimo habra que
encontrar una estructura de datos adecuada que permita la reutilizacion de los calculos de ecuacion en recurrencia, consiguiendo
una complejidad mejor que la del algoritmo puramente recursivo.

Siendo M la capacidad de la mochila y disponiendo de n elementos, llamaremos V(i,p) al valor maximo de la mochila con capacidad
p cuando consideramos i objetos, con 0<=p<=M y 1<=i<=n. La solucion viene dada por el valor de V(n,M). Denominaremos d1,d2,....,dn
a la secuencia de decisiones que conducen a obtener V(n,M), donde cada di podra tomar uno de los valores 1 o 0, dependiendo
si se introduce o no el i-esimo elemento. Podemos tener por tanto dos situaciones distintas:

1-Que dn=1. La subsecuencia de deciciones d1,d2,...,dn-1 ha de ser tambien optima para el problema V(n-1,M-1), ya que si no lo
fuera y existiera otra subsecuencia e1,e2,...,en-1 optima, la secuencia e1,e2,...,en-1, dn tambien seria optima para el problema
V(n,M) lo que contradice la hipotesis.

2-Que dn=0. Entonces la subsecuencia de decisiones d1,d2,...,dn-1 ha de ser tambien optima para el problema V(n-1,M).

Podemos aplicar por tanto el principio del optimo para formular la relacion en recurrencia. Teniendo en cuenta que en la mochila
no puede introducirse una fraccion del elemento sino que el elemento i se introduce o no se introduce, en una situacion cualquiera
V(i,p) tomara el valor mayor entre V(i-1,p), que indica que el elemento i no se introduce, y V(i-1,p-pi)+bi, que es el resultado
de introducirlo y de ahi que la capacidad ha de disminuir en pi y el valor aumentar en bi, y por tanto podemos plantear la solucion
al problema mediante la siguiente ecuacion:

                           ____________________________________________
                          |               
                          |0                             si i=0 y p>=0
                   V(i,p)=|-inf                          si p < 0
                          |Max{V(i-1,p),V(i-1,p-pi)+bi}  en otro caso
                          |____________________________________________

Estos valores se van almacenando en una tabla construida con el siguiente algoritmo:

TYPE TABLA=ARRAY[1..n],[0..M] OF CARDINAL;
     DATOS=RECORD peso, valor:CARDINAL; END;
     TIPOOBJETO=ARRAY[1..n] OF DATOS;

PROCEDURE Mochila(i,p:CARDINAL; VAR obj=TIPOOBJETO):CARDINAL;
    VAR elem, cap:CARDINAL; V:TABLA;
BEGIN
    FOR elem=1 TO i DO:
        V[elem,0]=0;
        FOR cap=1 TO p DO:
            IF (elem=1) AND (cap<obj[1].peso) THEN:
                V[elem, cap]=0
            ELSIF elem=1 THEN:
                V[elem, cap]=obj[1].valor
            ELSIF cap<obj[elem].peso THEN:
                V[elem, cap]= V[elem-1,cap]
            ELSE 
                V[elem, cap]=Max2(V[elem-1,cap],obj[elem].valor+V[elem-1,cap-obj[elem].peso])
            END
        END
    END;
    RETURN V[i,p]
END Mochila

EL problema se resuelve invocando a la funcion con i=n, p=M. La complejidad del algoritmo viene determinada por la construccion
de una tabla de dimensiones nxM y por tanto su tiempo de ejecucion es de orden de complejidad O(nM). La funcion max2 es la que 
calcula el maximo entre dos numeros naturales.
Si ademas del valor de la solucion optima se desea conocer los elementos que son introducidos, es decir, la composicion de la
mochila es necesario añadir al algoritmo la construccion de una tabla de valores logicos que indique para cada valor E[i,j]
si el elemento i forma parte de la solucion para la capcidad j o no:

TYPE ENTRAONO=ARRAY[1..N],[0..P] OF BOOLEAN;
PROCEDURE Max2especial(x,y:CARDINAL; VAR esmenorx:BOOLEAN):CARDINAL;
BEGIN
    IF x>y THEN:
        esmenorx=FALSE;
        RETURN x
    ELSE:
        esmenorx=TRUE;
        RETURN y
    END
END
PROCECUDE Mochila2(i,p:CARDINAL; obj: TIPOOBJETO; VAR E:ENTRAONO):CARDINAL;
    VAR elem, cap:CARDINAL;V:TABLA;
BEGIN
    FOR elem=1 TO i DO:
        V[elem,0]=0
        FOR cap=1 TO p DO:
            IF elem=1 and cap<obj[1].peso THEN:
                V[elem,cap]=0;
                E[elem,cap]=FALSE;
            ELSIF elem=1 THEN:
                V[elem,cap]=obj[1].valor;
                E[elem,cap]=TRUE;
            ELSIF cap<obj[elem].peso THEN:
                V[elem,cap]=V[elem-1,cap];
                E[elem,cap]=FALSE;
            ELSE:
                V[elem,cap]=Max2especial(V[elem-1,cap],obj[elem].valor+V[elem-1,cap-obj[elem].peso],E[elem,cap]);
            END
        END
    END;
    RETURN V[i,p]
END Mochila2;

Por otra parte, es necesario construir un algoritmo que interprete los valores de esta tabla para componer la solucion. Esto se
realizara recorriendola en sentido inverso desde los valores i=n, j=M hasta i=0, j=0, mediante el siguiente algoritmo:

TYPE SOLUCION=ARRAY[1..N] OF CARDINAL;
PROCEDURE Componer(VAR sol:SOLUCION);
    VAR elem,cap: CARDINAL;
BEGIN
    FOR elem=1 TO n DO:
        sol[elem]=0
    END;
    elem=n; cap=M;
    WHILE (elem<>0) AND (cap<>0) DO:
        IF E[elem,cap]:
            ....




'''
import numpy as np
# elementos que se desean hechar en la mochila.
Tipoobjeto = [(10, 10), (5, 100), (3, 3), (7, 200),
              (8, 15), (1, 50)]  # , (5, 6)]
# (PESO[0],BENEFICIO[1])


def Max2especial(x, y):
    if x > y:
        return x, False
    else:
        return y, True


def Mochila(i, p, obj):
    n = len(obj)
    M = 19  # peso maximo que puede sostener la mochila
    V = np.matrix(np.zeros((n, M)))
    E = np.full((n, M), False)
    for elem in range(i):
        V[elem, 0] = 0
        for cap in range(p):
            if elem == 0 and cap < obj[elem][0]:
                # condicion que entrara solo en la primera iteracion
                V[elem, cap] = 0
                E[elem, cap] = False
            elif elem == 0:
                # condicion que entrara solo en la primera iteracion
                V[elem, cap] = obj[elem][1]
                E[elem, cap] = True

            # cuando elem deja de ser 0 o la primera fila.
            elif cap < obj[elem][0]:
                V[elem, cap] = V[elem-1, cap]
                E[elem, cap] = False
            else:
                V[elem, cap], E[elem, cap] = Max2especial(
                    V[elem-1, cap], (obj[elem][1]+V[elem-1, cap-obj[elem][0]]))
    #print(V[elem])
    #print(E)
    solucionFinal(n,M,E,obj)
    return V[i-1, p-1]

def solucionFinal(n,M,E,obj):
    Sol=np.full(n,0)
    elem,cap=n-1,M-1
    while elem>0 and cap>0:
        if E[elem,cap]:
            Sol[elem]=1
            cap=cap-obj[elem][0]
        else:
            obj[elem]=0,0
        elem=elem-1
    for i in range(n):
        if Sol[i] != 1:
            obj[i]=0,0
    print(obj)

      

print(Mochila(6, 19, Tipoobjeto))
