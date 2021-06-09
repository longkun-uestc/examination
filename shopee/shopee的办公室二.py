data = input().split()
data = map(int, data)
X, Y, N = data
boss = set()
for i in range(N):
    x, y = map(int, input().split())
    boss.add((x, y))
grid = [[0 for i in range(Y+1)] for j in range(X+1)]
grid[X][Y] = 1
for i in range(X, -1, -1):
    for j in range(Y, -1, -1):
        if i == X and j == Y:
            continue
        if (i, j) in boss:
            grid[i][j] = 0
        elif i == X:
            grid[i][j] = grid[i][j+1]
        elif j == Y:
            grid[i][j] = grid[i+1][j]
        else:
            grid[i][j] = grid[i+1][j]+grid[i][j+1]
print(grid[0][0])







