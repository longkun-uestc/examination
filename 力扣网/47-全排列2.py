from typing import List
class Solution:
    pre = []
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.pre = []
        def dfs(nums, res):
            if not nums:
                self.pre.append(res[:])
                return
            nums.sort()
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                res.append(nums[i])
                dfs(nums[:i] + nums[i + 1:], res)
                res.pop()

        dfs(nums, [])
        return self.pre


if __name__ == '__main__':
    x = [1,2,1]
    s = Solution()
    r = s.permuteUnique(x)
    print(r)