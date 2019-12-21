class WildMatch:
    def chkWildMatch(self, A, lena, B, lenb):
        if lenb == 0 and lena > 0:
            return False
        if lena == 0 and lenb == 0:
            return True
        C = [[False for j in range(lenb+1)] for i in range(lena+1)]
        C[0][0] = True
        C[0][1] = False
        for i in range(1, lena+1):
            C[i][0] = False
        for j in range(2, lenb+1):
            if B[j-1] == "*":
                C[0][j] = C[0][j-2]
            else:
                C[0][j] = False
        for c in C:
            print(c)
        for i in range(1, lena+1):
            for j in range(1, lenb+1):
                if A[i-1]==B[j-1] or B[j-1] == ".":
                    C[i][j] = C[i-1][j-1]
                elif A[i-1] != B[j-1] and B[j-1] != "*":
                    C[i][j] = False
                elif B[j-1] == "*":
                    a = C[i][j-2]  # 产生0个
                    b = C[i][j-1]  # 产生1个
                    c = C[i-1][j] if A[i-1] == B[j-2] or B[j-2] == "." else False  # 产生多个。如果A的当前字符和B的前一个字符不相等，直接为False, 否则B不变，A前移一个字符
                    C[i][j] = a or b or c  # 最终结果为3种情况选1
                else:
                    print("error")
                    exit()
        print("---------------------------------")
        for c in C:
            print(c)
        print(C[lena][lenb])
        return C[lena][lenb]



if __name__ == '__main__':
    A = "aaa"
    B = "ab*ac*a*"
    s = WildMatch()
    s.chkWildMatch(A, len(A), B, len(B))
