# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        elif len(rotateArray) == 1:
            return rotateArray[0]
        else:
            left = 0
            right = len(rotateArray) - 1
            while left < right:
                mid = (left + right) // 2
                if rotateArray[mid] < rotateArray[right]:
                    right = mid
                elif rotateArray[mid] > rotateArray[right]:
                    left = mid + 1
                else:
                    right -= 1
            return rotateArray[left]


if __name__ == '__main__':
    # x = [3,4,5,1,2]
    x = [2, 2, 2, 2, 2, 2, 1, 2, 2, 2]  # left = 0, right =  9
    x = [2, 2, 1, 2, 2, 2, 2, 2, 2, 2]
    s = Solution()
    a = s.minNumberInRotateArray(x)
    print(a)
