class LCS:
    def findLCS(self, A, n, B, m):
        C = [[0 for i in range(m+1)] for j in range(n+1)]
        i, j = (n - 1, m - 1)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # print(i, j)
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                else:
                    C[i][j] = max(C[i - 1][j], C[i][j - 1], C[i - 1][j - 1])
        return C[n][m]


if __name__ == '__main__':
    s = LCS()
    A = "1A2C3D4B56"
    B = "B1D23CA45B6A"
    s.findLCS(A, 10, B, 12)
