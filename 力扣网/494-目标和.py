from typing import List
class Solution:
    count = 0
    def findTargetSumWays1(self, nums: List[int], target: int) -> int:
        self.count = 0
        def dfs(nums, target, index, s):
            if index == len(nums):
                if s == target:
                    self.count += 1
            else:
                dfs(nums, target, index+1, s+nums[index])
                dfs(nums, target, index+1, s-nums[index])
        dfs(nums, target, 0, 0)
        return self.count

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [dict() for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                dp[i][-nums[i]] = 1
                if nums[i] not in dp[i]:
                    dp[i][nums[i]] = 1
                else:
                    dp[i][nums[i]] += 1
                continue
            if nums[i] == 0:
                for k,v in dp[i-1].items():
                    dp[i][k] = v*2
                continue
            for s in dp[i - 1].keys():
                if s - nums[i] not in dp[i]:
                    dp[i][s - nums[i]] = dp[i - 1][s]
                else:
                    dp[i][s - nums[i]] += dp[i-1][s]
                if s + nums[i] not in dp[i]:
                    dp[i][s + nums[i]] = dp[i - 1][s]
                else:
                    dp[i][s + nums[i]] += dp[i-1][s]
        for i, d in enumerate(dp):
            print(i,nums[i], "----------------")
            for k,v in d.items():
                print(k, v)
        if target in dp[len(nums)-1]:
            return dp[len(nums)-1][target]
        else:
            return 0



if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,1]
    target = 3
    nums = [0,0,0,0,0,0,0,0,1]
    target = 1
    # nums = [9,7,0,3,9,8,6,5,7,6]
    # target = 2
    r = s.findTargetSumWays(nums, target)
    print(r)