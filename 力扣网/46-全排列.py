from typing import List
class Solution:
    pre = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.pre = []
        def dfs(nums, res):
            if not nums:
                self.pre.append(res[:])
                return
            for i, n in enumerate(nums):
                res.append(n)
                dfs(nums[:i]+nums[i+1:], res)
                res.pop()
        dfs(nums, [])
        return self.pre

if __name__ == '__main__':
    x = [1,2,3]
    s = Solution()
    r = s.permute(x)
    print(r)