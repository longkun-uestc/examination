class Matrix:
    def __init__(self, N, M, K, mat):
        self.N = N
        self.M = M
        self.K = K
        self.mat = mat
        self.dp = [[[0 for i in range(K+1)] for j in range(M)] for k in range(N)]

    def search_all(self):
        max_count = -1
        for i in range(N):
            for j in range(M):
                max_count = max(max_count, self.search_method(i,j,self.K))
        return max_count

    def search_method(self, n, m, k):
        if n<0 or m<0 or k<0:
            return 0
        if self.dp[n][m][k] != 0:
            return self.dp[n][m][k]
        if n - 1 >= 0 and self.mat[n - 1][m] > self.mat[n][m]:
            c1 = self.search_method(n - 1, m, k)
        elif n - 1 >= 0 and k > 0:
            c1 = self.search_method(n - 1, m, k - 1)
        else:
            c1 = 0
        if n + 1 < len(self.mat) and self.mat[n + 1][m] > self.mat[n][m]:
            c2 = self.search_method(n + 1, m, k)
        elif n + 1 < len(self.mat) and k > 0:
            c2 = self.search_method(n + 1, m, k - 1)
        else:
            c2 = 0
        if m - 1 >= 0 and self.mat[n][m - 1] > self.mat[n][m]:
            c3 = self.search_method(n, m - 1, k)
        elif m - 1 >= 0 and k > 0:
            c3 = self.search_method(n, m - 1, k - 1)
        else:
            c3 = 0
        if m + 1 < len(self.mat[0]) and self.mat[n][m + 1] > self.mat[n][m]:
            c4 = self.search_method(n, m + 1, k)
        elif m + 1 < len(self.mat[0]) and k > 0:
            c4 = self.search_method(n, m + 1, k - 1)
        else:
            c4 = 0
        self.dp[n][m][k] = max(c1, c2, c3, c4) + 1
        return self.dp[n][m][k]
        



if __name__ == '__main__':
    N, M, K = list(map(int, input().split(' ')))
    mat = []
    for i in range(N):
        a = list(map(int, input().split(' ')))
        mat.append(a)

    matrix = Matrix(N, M, K, mat)
    b = matrix.search_all()
    print(b)
