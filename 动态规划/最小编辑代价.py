class MinCost:
    def findMinCost(self, A, n, B, m, c0, c1, c2):
        C = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(0, n + 1):
            C[i][0] = i * c1
        for j in range(0, m + 1):
            C[0][j] = j * c0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1]
                else:
                    C[i][j] = min(C[i][j - 1] + c0, C[i - 1][j] + c1, C[i - 1][j - 1] + c2)
        # for c in C:
        #     print(c)
        # print(C[n][m])
        return C[n][m]


if __name__ == '__main__':
    s = MinCost()
    a = "ccbbbcba"
    b = "cbbaacbc"
    a = "bbca"
    b = "cabacab"
    # a = "abc"
    # b = "adc"
    s.findMinCost(a, len(a), b, len(b), 1, 2, 7)
