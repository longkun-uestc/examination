from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        while start < end:
            if nums[start] < nums[end]:
                return nums[start]
            mid = (start + end) // 2
            if nums[start] < nums[mid]:
                start = mid
            elif nums[start] == nums[mid]:
                start += 1
            elif nums[end] > nums[mid]:
                end = mid
            elif nums[end] == nums[mid]:
                end -= 1
        return nums[start]


if __name__ == '__main__':
    s = Solution()
