import numpy as np 
import networkx as nx 

parent=dict()#diccionario de nombre parent
rank=dict()#diccionario de nombre rank

def make_set(vertice):
    parent[vertice]=vertice#clave vertice, valor de la clave vertice
    rank[vertice]=0

def find(vertice):
    if parent[vertice] is not vertice:
        parent[vertice] is find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1=find(vertice1)
    root2=find(vertice2)
    if root1 is not root2:
        if rank[root1]>rank[root2]:
            parent[root2]=root1
        else:
            parent[root1]=root2
        if rank[root1] is rank[root2]:
            rank[root2]+=1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
        minimun_spanning_tree=set()
        edges=list(graph['edges'])
        edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) is not find(vertice2):
            union(vertice1, vertice2)
            minimun_spanning_tree.add(edge)
    return sorted(minimun_spanning_tree)
graph={
    'vertices': ['A', 'B', 'C', 'D'],
    'edges': set([
        (1, 'A','B'),
        (2,'A','C'),
        (3,'A','D'),
        (4,'B','C'),
        (2,'B','D'),
        (1,'C','D'),
    ])
}
def generador_1(MatrizAbya):
    letras=['A','B','C','D','E','F','G','H','I','J','K','L','M']
    letras=letras[0:len(MatrizAbya[0,:])]
    for i in range(0,len(MatrizAbya[0,:])):
        if MatrizAbya[i,i] is 0:
            for j in range(i+1, len(MatrizAbya[0,:])):
                

print(kruskal(graph))
M=np.array([[0,1,5,0,0,0],[1,0,2,5,2,0],[5,2,0,0,2,0],[0,5,0,0,1,2],[0,2,2,1,0,4],[0,0,0,2,4,0]])
Graph=np.array([[0,1,2,3],[1,0,4,2],[2,4,0,1],[3,2,1,0]])
print(M)
print(Graph)