import math
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, int(math.sqrt(n))+1):
            dp[i**2] = 1
        for i in range(1, n+1):
            if dp[i] == 0:
                min_c = 100000
                for j in range(1, math.ceil(math.sqrt(i))):
                    min_c = min(min_c, dp[i-j**2])
                dp[i] = min_c+1
        return dp[n]

if __name__ == '__main__':
    n = 11
    s = Solution()
    r = s.numSquares(n)
    print(r)







