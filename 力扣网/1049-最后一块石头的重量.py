from typing import List
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n, m = len(stones), total//2
        dp = [[False for j in range(m+1)] for i in range(n+1)]
        dp[0][0] = True
        for i in range(1, n+1):
            for j in range(0, m+1):
                if stones[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-stones[i-1]]
        max_j = -1
        for j in range(m+1):
            if dp[n][j]:
                max_j = max(max_j, j)
        diff = total-2*max_j
        return diff

if __name__ == '__main__':
    x = [2,7,4,1,8,1]
    # x = [2,2]
    x = [31,26,33,21,40]
    s = Solution()
    r = s.lastStoneWeightII(x)
    print(r)

