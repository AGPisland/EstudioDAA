import numpy as np


def isSafe(x, y, sol):
    N = len(sol)
    return (x >= 0 and x < N and y >= 0 and y < N and sol[x][y] == -1)


def solver(N):
    sol = np.ones((N, N), dtype=int)*-1
    print(sol)
    xMove = [2, 1, -1, -2, -2, -1,  1,  2]
    yMove = [1, 2,  2,  1, -1, -2, -2, -1]
    sol[0][0] = 0
    if solverUtil(0, 0, 1, sol, xMove, yMove) == False:
        print("no hay solucion")
        return False
    else:
        print(sol)
    return True


def solverUtil(x, y, movei, sol, xMove, yMove):
    N = len(sol)
    if movei == N*N:
        return True
    for k in range(8):
        next_x = x+xMove[k]
        next_y = y+yMove[k]
        if isSafe(next_x, next_y, sol):
            sol[next_x][next_y] = movei
            if solverUtil(next_x, next_y, movei+1, sol, xMove, yMove):
                return True
            else:
                sol[next_x][next_y] = -1

    return False


if __name__ is '__main__':
    solver(5)
