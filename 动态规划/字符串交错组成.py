class Mixture:
    def chkMixture(self, A, n, B, m, C, v):
        if n == 0 and m == 0 and v == 0:
            return True
        if n == 0 and B != C:
            return False
        if m == 0 and A != C:
            return False
        if n == 0 and m == 0 and v != 0:
            return False
        if v != n + m:
            return False
        M = [[False for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            if A[i-1] == C[i-1]:
                M[i][0] = True
        for j in range(1, m + 1):
            if B[j-1] == C[j-1]:
                M[0][j] = True
        M[0][0] = True
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    if C[i + j - 1] == A[i - 1]:
                        M[i][j] = M[i][j - 1] or M[i - 1][j]
                    else:
                        M[i][j] = False
                else:
                    if C[i + j - 1] == A[i - 1]:
                        M[i][j] = M[i - 1][j]
                    elif C[i + j - 1] == B[j - 1]:
                        M[i][j] = M[i][j - 1]
                    else:
                        M[i][j] = False
        for a in M:
            print(a)
        print(M[n][m])
        return M[n][m]

if __name__ == '__main__':
    s = Mixture()
    # A = "ABC"
    # B = "12C"
    # C = "A12CCB"
    A = "bcbccabccacccbcac"
    B = "abbbacaabccbccaaaabbcbcbaaacccbaaba"
    C = "babbbacaabccbccaaaabbcbcbaaacccbaabacbccabccacccbcac"
    s.chkMixture(A, len(A), B, len(B), C, len(C))

