import random
def get_around(mat, x, y):
    s = mat[x][y]
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    count = 1
    for m in move:
        if 0 <= x + m[0] < len(mat) and 0 <= y + m[1] < len(mat[0]):
            s += mat[x + m[0]][y + m[1]]
            count += 1
    return round(s / count)


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    mat = []
    for i in range(n):
        # a = list(map(int, input().split()))
        a = [random.randint(0, 255) for j in range(m)]
        mat.append(a)
    print(mat)
    for m1 in mat:
        s = ' '.join(map(str, m1))
        print(s)

    print("------------------")
    move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for i in range(n):
        for j in range(m):
            s = mat[i][j]
            count = 1
            for mv in move:
                if 0 <= i + mv[0] < n and 0 <= j + mv[1] < m:
                    s += mat[i + mv[0]][j + mv[1]]
                    count += 1
            mat[i][j] = round(s / count)
            # mat[i][j] = get_around(mat, i, j)
    for m in mat:
        s = " ".join(map(str, m))
        print(s)
