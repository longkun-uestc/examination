def get_max(array):
    dp = [[0 for i in range(len(array))] for j in range(len(array))]
    M = [[-1 for i in range(len(array))] for j in range(len(array))]
    max_val = 0
    for i in range(len(array)):
        dp[i][i] = 0
        M[i][i] = array[i]
    for i in range(len(array) - 1):
        if array[i] == array[i + 1]:
            dp[i][i + 1] = 1
            M[i][i + 1] = array[i] + 1
            max_val = 1
    for r in range(3, len(array) + 1):
        for i in range(len(array) - r + 1):
            j = i + r - 1
            a = []
            for k in range(i + 1, j):
                if M[i][k] == M[k + 1][j]:
                    val = dp[i][k] + dp[k + 1][j]+1
                    m = M[i][k] + 1
                    a.append((val, m))
            if not a:
                dp[i][j] = 0
                M[i][j] = -1
            else:
                a.sort(key=lambda x: x[0])
                dp[i][j] = a[0][0]
                M[i][j] = a[0][1]
            max_val = max(max_val, dp[i][j])
    # for p in dp:
    #     print(p)
    # print("--------")
    # for m in M:
    #     print(m)
    return max_val


if __name__ == '__main__':
    N = int(input())
    array = list(map(int, input().split()))
    res = get_max(array)
    print(res)
