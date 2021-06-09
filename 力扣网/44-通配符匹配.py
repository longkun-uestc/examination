class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if not s and p == "*":
            return True
        if s and not p:
            return False
        dp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == "*":
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(p)+1):
            for j in range(1, len(s)+1):
                if p[i-1] == s[j-1] or p[i-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == "*":
                    a = dp[i][j-1]
                    b = dp[i-1][j-1]
                    c = dp[i-1][j]
                    dp[i][j] = a or b or c

        for d in dp:
            print(d)
        return dp[len(p)][len(s)]






if __name__ == '__main__':
    a = "acdcb"
    b = "a*c?b"
    s = Solution()
    r = s.isMatch(a, b)
    print(r)

