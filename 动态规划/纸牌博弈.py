class Cards:
    def cardGame(self, A, n):
        if n <= 0:
            return 0
        M = [[0 for i in range(n)] for j in range(n)]
        F = [["0" for i in range(n)] for j in range(n)]
        for i in range(n):
            M[i][i] = A[i]
            F[i][i] = "L"
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                M[i][i + 1] = A[i]
                F[i][i + 1] = "L"
            else:
                M[i][i + 1] = A[i + 1]
                F[i][i + 1] = "R"
        for r in range(3, n + 1):
            for i in range(n - r + 1):
                j = i + r - 1
                if F[i + 1][j] == "L":
                    left = A[i] + M[i + 2][j]
                else:
                    left = A[i] + M[i + 1][j - 1]
                if F[i][j - 1] == "L":
                    right = A[j] + M[i + 1][j - 1]
                else:
                    right = A[j] + M[i][j - 2]

                if left >= right:
                    M[i][j] = left
                    F[i][j] = "L"
                else:
                    M[i][j] = right
                    F[i][j] = "R"
        # print("-----------------------")
        # for m in M:
        #     print(m)
        # for f in F:
        #     print(f)
        a = M[0][n - 1]
        b = sum(A) - a
        result = a if a > b else b
        print(result)
        return result


if __name__ == '__main__':
    s = Cards()
    x = [1, 2, 100, 4, 15]
    s.cardGame(x, len(x))
