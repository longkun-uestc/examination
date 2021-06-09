def bag(n, m, array):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for t in range(1, m+1):
        for i in range(1, n+1):
            if t < array[i-1][0]:
                dp[t][i] = dp[t][i-1]
            else:
                dp[t][i] = max(dp[t-array[i-1][0]][i-1]+array[i-1][1], dp[t][i-1])
    # for d in dp:
    #     print(d)
    return dp[m][n]



if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    array = []
    for i in range(n):
        x = list(map(int, input().split()))
        array.append(x)
    array.sort(key=lambda x:x[0])
    res = bag(n, m, array)
    print(res)

