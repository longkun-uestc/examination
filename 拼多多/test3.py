def get_dp(n, m, K):
    dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        if i == K:
            print('a' * K)
            return
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            count = dp[0][j] + i
            for k in range(1, i + 1):
                count += dp[k][j - 1] + 1
            dp[i][j] = count
    j = 0
    while j < len(dp[0]) and dp[n][j] < K:
        j += 1
    s = find1(dp, n, j, K)
    print(s)

def find1(dp, n, m, K):
    if K <= n:
        return "a" * K
    elif n < K <= m:
        return 'a' * n + 'b' * (K - n)
    else:
        K = K-n-m
        for i in range(1, n+1):
            if K <= dp[i][m-1] + 1:
                head = 'a'*(n-i) + 'b'
                s = find1(dp, i, m-1, K-1)
                new_s = head+s
                return new_s
            else:
                K = K-dp[i][m-1]-1








if __name__ == '__main__':
    N, M, K = list(map(int, input().split()))
    get_dp(N, M, K)
