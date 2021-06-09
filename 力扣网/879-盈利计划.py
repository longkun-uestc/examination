from typing import List
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0 for k in range(minProfit+1)]for j in range(n+1)]for i in range(len(group)+1)]
        dp[0][0][0] = 1
        for i in range(len(group)+1):
            dp[i][0][0] = 1
        for j in range(n+1):
            dp[0][j][0] = 1

        for i in range(1, len(group)+1):
            for j in range(1, n+1):
                for k in range(minProfit+1):
                    if group[i-1] > j:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = (dp[i-1][j-group[i-1]][0] if profit[i-1]>=k else dp[i-1][j-group[i-1]][k-profit[i-1]]) + dp[i-1][j][k]
                        # if profit[i-1] >= k:
                        #     dp[i][j][k] = dp[i-1][j-group[i-1]][0] + dp[i-1][j][k]
                        # else:
                        #     dp[i][j][k] = dp[i-1][j-group[i-1]][k-profit[i-1]] + dp[i-1][j][k]
        return dp[len(group)][n][minProfit] % (10**9+7)

if __name__ == '__main__':
    n = 10
    minProfit = 5
    group = [2,3,5]
    profit = [6,7,8]
    n = 5
    minProfit = 3
    group = [2, 2]
    profit = [2, 3]
    s = Solution()
    r = s.profitableSchemes(n, minProfit, group, profit)
    print(r)




