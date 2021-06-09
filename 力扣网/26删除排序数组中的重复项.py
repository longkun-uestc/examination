from typing import List
class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        i = 1
        end = len(nums)
        while i < end:
            if nums[i] == nums[i-1]:
                j = i + 1
                while j < end:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    j += 1
                end -= 1
            else:
                i += 1
        nums = nums[:end]
        return end

    def removeDuplicates2(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] is True:
                i += 1
                continue
            j = 1
            while i + j < len(nums) and nums[i] == nums[i+j]:
                nums[i+j] = True
                j += 1
            i += 1
        # print(nums)
        i = 1
        while i < len(nums):
            if nums[i] is True:
                j = i+1
                while j < len(nums) and nums[j] is True:
                    j += 1
                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    break
                i += 1
            else:
                i += 1
        # print(nums)
        print(i)
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j == len(nums):
                break
            nums[i+1] = nums[j]
            i += 1
            j += 1
        return i + 1

if __name__ == '__main__':
    s = Solution()
    x = [0,0,1,1,2,2,3,4,5]
    # x = [0,0,0,0,0,0,0,0]
    res = s.removeDuplicates(x)
    print(res)