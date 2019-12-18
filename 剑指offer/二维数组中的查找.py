# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        if len(array) == 0 or len(array[0]) == 0:
            return False
        if target < array[0][0]:
            return False
        if target > array[-1][-1]:
            return False
        p1 = len(array)-1
        p2 = 0
        while ((p1 >= 0) and (p2 < len(array[0]))):
            if target < array[p1][p2]:
                p1 -= 1
            elif target > array[p1][p2]:
                p2 += 1
            elif target == array[p1][p2]:
                return True
        return False
        # write code here


if __name__ == '__main__':
    x = [[1, 3, 4, 6],
         [2, 4, 8, 10],
         [3, 5, 9, 13],
         [4, 6, 10, 15]]
    s = Solution()
    result = s.Find(14, x)
    print(result)

