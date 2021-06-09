if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    score = [[float('inf') for i in range(n)] for j in range(n)]
    score[0][0] = 0
    queue = [(0, 0)]
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while queue:
        x, y = queue.pop(0)
        for mv in move:
            new_x, new_y = x + mv[0], y + mv[1]
            if 0 <= new_x < n and 0 <= new_y < n:
                new_score = score[x][y] + abs(mat[x][y] - mat[new_x][new_y])
                if new_score < score[new_x][new_y]:
                    score[new_x][new_y] = new_score
                    queue.append((new_x, new_y))
    print(score[n-1][n-1])