from typing import List
from collections import defaultdict
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, tmp):
            if len(tmp) > 1:
                res.append(tmp[:])
            pre_idx = defaultdict(int)
            for idx, n in enumerate(nums):
                if pre_idx[n]:
                    continue
                if not tmp or n >= tmp[-1]:
                    pre_idx[n] = 1
                    dfs(nums[idx+1:], tmp+[n])
        dfs(nums, [])
        return res

