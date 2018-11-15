Sudok =  [0, 1, 2, 3, 4, 5, 6, 7, 8
        _____________________________
        0[5| 1| 7|, 6|<8|<9|,<2| 3| 4],
        1[2| 8| 9|,<3|(7| 4|,<1|(0|(0],
        2[3| 4| 6|, 2|(0| 5|,(0| 9| 0],
        3[6, 0, 2,  0, 0, 0,  0, 1, 0],
        4[0, 3, 8,  0, 0, 6,  0, 4, 7],
        5[0, 0, 0,  0, 0, 0,  0, 0, 0],
        6[0, 9, 0,  0, 0, 0,  0, 7, 8],
        7[7, 0, 3,  4, 0, 0,  5, 6, 0],
        8[0, 0, 0,  0, 0, 0,  0, 0, 0]
        ]

import os
os.system('cls')
def findNextCellToFill(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y #0,4, <0,5, <0,6, <1,6,<1,3,<1,4,<1,7,<1,8
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1 #  completa la matriz solucion

def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    # si e no se encuentra en la fila retornamos true
    if ro wOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        # si e no se encuentra en la columna retornamos true
        # se encontrara en en el cubo 3x3 solo falta verificar los 4 cuadrados
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if grid[x][y] == e:
                        return False
            return True
    return False
#retorna true ssi e no esta repetida en fila columna y 3x3
def solveSudoku(grid, i=0, j=0):
    i,j = findNextCellToFill(grid, i, j)#0,4, < 0,5, <0,6, <1,3,<1,4,<1,7,<1,8,<2,4,<2,6
    if i == -1:
        return True
    for e in range(1,10):
        if isValid(grid,i,j,e):#(0,4,8),<(0,5,9), <(0,6,2),<(1,6,1),<(1,3,3),<(1,4,6),(1,7,5),(1,8,null),Bck,(1,7,0)
            #,(1,7,null),Bck,(1,4,0),(1,4,7),<(1,7,5),<(1,8,6),<(2,4,1),<(2,6,)
            #Retorna true si e no se repite en C,F y Mm 3x3
            grid[i][j] = e
            #un candidato para seguir, aqui se ramifica el arbol.
            if solveSudoku(grid, i, j):#(0,4),<(0,5), <(0,6), <(1,6),<(1,3),<(1,4),<(1,7),<(1,6),<(2,4)
            #falso ya que el 1,8 no hay otra opcion
                return True
                # Undo the current cell for backtracking
            grid[i][j] = 0
    return False
