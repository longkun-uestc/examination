from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1) + len(nums2)) / 2
        if mid - int(mid) == 0:
            mid1 = int(mid)
            mid2 = int(mid) + 1
            s1 = self.get_k(nums1, nums2, mid1)
            s2 = self.get_k(nums1, nums2, mid2)
            return (s1 + s2)/2
        else:
            mid1 = int(mid) + 1
            return self.get_k(nums1, nums2, mid1)

    def get_k(self, nums1, nums2, k):
        if not nums1:
            return nums2[k-1]
        if not nums2:
            return nums1[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        mid = k//2
        idx1 = min(len(nums1)-1, mid-1)
        idx2 = min(len(nums2)-1, mid-1)
        if nums1[idx1] <= nums2[idx2]:
            return self.get_k(nums1[idx1+1:], nums2, k-idx1-1)
        else:
            return self.get_k(nums1, nums2[idx2+1:], k-idx2-1)

if __name__ == '__main__':
    s1 = [1,2,3,4,5,6]
    s2 = [3,4,5,6,7,8]
    s = Solution()
    res = s.get_k(s1, s2, 7)
    print(res)
