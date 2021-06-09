from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums)-1
        while end > 0 and nums[end] <= nums[end-1]:
            end -= 1
        if end > 0:
            j = len(nums)-1
            while j >= end and nums[j] <= nums[end-1]:
                j += 1
            nums[end-1], nums[j] = nums[j], nums[end-1]
        for i in range(end, len(nums)):
            for k in range(i + 1, len(nums)):
                if nums[i] > nums[k]:
                    nums[i], nums[k] = nums[k], nums[i]


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,4,5,3]
    # nums = [5,4,3,2,1]
    nums = [1,2,3]
    s.nextPermutation(nums)
    print(nums)
