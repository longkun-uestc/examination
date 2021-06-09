from typing import List
class Solution:
    map_dict = {}
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        flag = [False for i in range(len(nums))]
        res = [0 for i in range(len(nums))]
        flag[-1] = True
        res[-1] = nums[-1]
        res[-2] = max(nums[-1], nums[-2])
        flag[-2] = True if res[-2] == res[-1] else False
        for idx in range(len(nums)-3, -1, -1):
            v1 = nums[idx] + res[idx+2]
            v2 = res[idx+1]
            res[idx] = max(v1, v2)
            flag[idx] = flag[idx+2] if res[idx] == v1 else flag[idx+1]
        if flag[0] == flag[-1]:
            max_c = max(res[0]-nums[0], res[0]-nums[-1])
            max_c = max(max_c, res[1])
        else:
            max_c = res[1]
        return max_c

        # self.map_dict = {}
        # v = self.get_max(nums, 0)
        # return v

    def get_max(self, nums, idx):
        if idx >= len(nums):
            return 0
        v1 = self.map_dict[idx+1] if idx+1 in self.map_dict else self.get_max(nums, idx+1)
        v2 = self.map_dict[idx+2] if idx+2 in self.map_dict else self.get_max(nums, idx+2)
        val = max(nums[idx]+v2, v1)

        self.map_dict[idx] = val
        return val

if __name__ == '__main__':
    s = Solution()
    nums = [1, 100, 2, 3, 200, 1, 1]
    # nums = [2, 3, 2]
    res = s.rob(nums)
    print(res)

