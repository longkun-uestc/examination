if __name__ == '__main__':
    n = int(input())
    mat = [[0 for i in range(n)] for j in range(n)]
    flag = 1 if n % 2 == 1 else 0
    for i in range(n // 2 - 1):
        for j in range(n // 2 - 1 - i):
            mat[i][n // 2 + j + flag] = 1
            mat[i][n // 2 - 1 - j] = 2
            mat[n // 2 - 1 - i][j] = 3
            mat[n // 2 + i + flag][j] = 4
            mat[n - 1 - i][n // 2 - 1 - j] = 5
            mat[n - 1 - i][n // 2 + j + flag] = 6
            mat[n // 2 + i+flag][n - 1 - j] = 7
            mat[n // 2 - 1 - i][n - 1 - j] = 8
    for m in mat:
        s = ' '.join(map(str, m))
        print(s)
