def max_count(array):
    count = {}
    for x in array:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    max_cnt = -1
    k = ''
    for key, val in count.items():
        if val > max_cnt:
            max_cnt = val
            k = key
    return max_cnt, k
def search(a, n, m):
    dp = [[False for i in range(n)] for j in range(n)]
    for i in range(n):
        dp[i][i] = False
    # for i in range(n-1):
    #     j = i+1
    #     if m == 1:
    #         dp[i][j] = True
    #     else:
    #         dp[i][j] = False
    for r in range(2, n+1):
        L = n - r + 1
        for i in range(L):
            j = i + r - 1
            dp[i][j] = dp[i+1][j] or dp[i][j-1]
            if not dp[i][j]:
                arr = a[i:j+1]
                max_cnt = max(a[i+1:j+1].count(a[i]) + 1, a[i:j].count(a[j])+1)
                if max_cnt >= m:
                    dp[i][j] = True
    for d in dp:
        print(d)



if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    search(a, n, m)