class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)):
            M[i][0] = 1
        for i in range(1, len(t)):
            M[0][i] = 0
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    M[i][j] = M[i-1][j] + M[i-1][j-1]
                else:
                    M[i][j] = M[i-1][j]
        for i in range(len(s)+1):
            print(M[i])
        return M[len(s)][len(t)]

    def numDistinct1(self, s: str, t: str) -> int:
        # print(s, t)
        if len(t) == 0:
            return 1
        if len(s) < len(t):
            return 0
        if s[-1] != t[-1]:
            return self.numDistinct1(s[:-1], t)
        else:
            return self.numDistinct1(s[:-1], t) + self.numDistinct1(s[:-1], t[:-1])


if __name__ == '__main__':
    a = "rabbbit"
    b = "rabbit"
    a = "babgbag"
    b = "bag"
    a = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    b = "bddabdcae"
    s = Solution()
    c = s.numDistinct(a, b)
    print(c)
