import numpy as np

grid = [[0, 0, 6, 0, 0, 0, 7, 5, 1],
        [2, 0, 0, 7, 0, 0, 0, 9, 0],
        [0, 5, 0, 0, 0, 6, 4, 8, 0],
        [9, 0, 2, 0, 7, 0, 0, 0, 4],
        [3, 7, 4, 0, 0, 0, 8, 0, 0],
        [1, 8, 5, 4, 2, 9, 0, 0, 7],
        [0, 0, 1, 9, 0, 0, 0, 7, 0],
        [0, 0, 9, 0, 5, 0, 1, 0, 0],
        [0, 2, 7, 6, 0, 3, 0, 4, 5]]

print(np.matrix(grid), end="now solved \n")


def possible(y: int, x: int, n: int):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False

    for i in range(0, 9):
        if grid[i][x] == n:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True


def solve() :
    global grid
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0

                return

    print(np.matrix(grid))


solve()
print('this is ths sudoku solve')




