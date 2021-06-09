from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        idx = self.get_k(nums, 0, len(nums) - 1, len(nums) - k)
        return nums[idx]

    def get_k(self, nums, start, end, k):
        idx = self.div(nums, start, end)
        if idx == k:
            return idx
        if idx < k:
            return self.get_k(nums, idx+1, end, k)
        else:
            return self.get_k(nums, start, idx-1, k)

    def div(self, nums, start, end):
        i, j = start, end
        now = nums[start]
        while i < j:
            while j > i and nums[j] > now:
                j -= 1
            if j > i:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] <= now:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1
        nums[i] = now
        return i

if __name__ == '__main__':
    s = Solution()
    x = [3,2,1,5,6,4]
    r = s.findKthLargest(x, 4)
    print(r)