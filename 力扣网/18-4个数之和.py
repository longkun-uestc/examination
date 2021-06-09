from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue
            tag0 = target - nums[first]
            for second in range(first+1, n):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue
                tag1 = tag0 - nums[second]
                third = second + 1
                forth = n-1
                while third < forth:
                    s = nums[third] + nums[forth]
                    if s == tag1:
                        res.append([nums[first], nums[second], nums[third], nums[forth]])
                        third0 = third + 1
                        while third0 < n and nums[third0] == nums[third0 - 1]:
                            third0 += 1
                        third = third0
                        forth0 = forth - 1
                        while forth0 > third and nums[forth0] == nums[forth0 + 1]:
                            forth0 -= 1
                        forth = forth0
                    elif s < tag1:
                        third0 = third + 1
                        while third0 < n and nums[third0] == nums[third0-1]:
                            third0 += 1
                        third = third0
                    else:
                        forth0 = forth - 1
                        while forth0 > third and nums[forth0] == nums[forth0+1]:
                            forth0 -= 1
                        forth = forth0
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [-1,0,-5,-2,-2,-4,0,1,-2]
    target = -9
    r = s.fourSum(nums, target)
    print(r)
