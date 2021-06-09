if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    mat = [[0 for i in range(2 * n - 1)] for j in range(n)]
    mat[0][0] = int(arr[0][0])
    for i in range(n - 1):
        for j in range(len(arr[i])):
            mat[i+1][j] = max(mat[i+1][j], mat[i][j] + arr[i+1][j])
            mat[i+1][j+1] = max(mat[i+1][j+1], mat[i][j] + arr[i+1][j+1])
            mat[i+1][j+2] = max(mat[i+1][j+2], mat[i][j] + arr[i+1][j+2])
    # for m in mat:
    #     print(m)
    print(max(mat[-1]))

# 4
# 3
# 594
# 52139
# 3728426