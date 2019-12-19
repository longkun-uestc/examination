class LongestSubstring:
    def findLongest(self, A, n, B, m):
        C = [[0 for i in range(m + 1)] for j in range(n + 1)]
        max_len = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1  # max(C[i - 1][j - 1] + 1, C[i - 1][j], C[i][j - 1])
                else:
                    C[i][j] = 0  # max(C[i - 1][j - 1], C[i - 1][j], C[i][j - 1])
                if C[i][j] > max_len:
                    max_len = C[i][j]
        # for c in C:
        #     print(c)
        # print(max_len)
        return max_len


if __name__ == '__main__':
    s = LongestSubstring()
    A = "1AB2345CD"
    B = "12345EF"
    s.findLongest(A, 9, B, 7)
