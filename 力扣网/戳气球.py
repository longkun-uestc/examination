from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for i in range(len(nums))] for j in range(len(nums))]
        for r in range(3, len(nums)+1):
            for i in range(0, len(nums) - r+1):
                j = i + r-1
                dp[i][j] = max([(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]) for k in range(i+1, j)])
        for d in dp:
            print(d)
        return dp[0][len(nums)-1]



if __name__ == '__main__':
    s = Solution()
    x = [3, 1, 5, 8]
    a = s.maxCoins(x)
    print(a)