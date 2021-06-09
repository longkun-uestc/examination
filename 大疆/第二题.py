def max_val(arr, N, X):
    dp = [[0 for j in range(N+1)] for i in range(X+1)]
    for i in range(1, X+1):
        for j in range(1, N+1):
            if i < arr[j-1][0]:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = max(dp[i-arr[j-1][0]][j-1]+arr[j-1][1], dp[i][j-1])
    # for d in dp:
    #     print(d)
    return dp[X][N]

if __name__ == '__main__':
    N, X = list(map(int, input().split()))
    arr = []
    for i in range(N):
        val, t = list(map(int, input().split()))
        arr.append([t, val])
    arr.sort(key=lambda x: x[0])
    res = max_val(arr, N, X)
    print(res)
