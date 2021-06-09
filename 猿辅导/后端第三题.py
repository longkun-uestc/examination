def get_min(n, K):
    if K >= n-1:
        return 0
    dp = [[[0 for i in range(K+1)]for j in range(n)] for x in range(n)]
    for i in range(n):
        dp[i][i][0] = 0
    for i in range(n-1):
        dp[i][i+1][0] = i+1
    for r in range(3, n+1):
        for i in range(n-r+1):
            j = i + r - 1
            dp[i][j][0] = dp[(i+j)//2+1][j][0] + (i+j)//2 + 1
            m = []
            for h in range(i+1, j):
                m.append(dp[i][h][0] + dp[h+1][j][0])
            dp[i][j][0] = min(m) 
            for k in range(1, K+1):
                if k >= (j-i):
                    dp[i][j][k] = 0
                else:
                    dp[i][j][k] = min(dp[(i+j)//2+1][j][k-1], dp[(i+j)//2+1][j][k]+(i+j)//2 + 1)
    return dp[0][n-1][K]




if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    res = get_min(n, k)
    print(res)
