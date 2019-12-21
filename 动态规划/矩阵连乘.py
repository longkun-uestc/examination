class Solution:
    def matrix_multiply(self, matrix_list):
        if len(matrix_list) == 0:
            return 0
        n = len(matrix_list)
        M = [[0 for i in range(n)] for j in range(n)]
        for r in range(2, n+1):
            for i in range(n - r + 1):
                left = matrix_list[i]
                j = i+r-1
                right = matrix_list[j]
                M[i][j] = min([M[i][k] + M[k + 1][j] + left[0] * matrix_list[k][1] * right[1] for k in range(i, j)])
        for m in M:
            print(m)
        return M[0][n-1]


if __name__ == '__main__':
    s = Solution()
    x = [(30, 35), (35, 15), (15, 5), (5, 10), (10, 20), (20, 25)]
    s.matrix_multiply(x)
