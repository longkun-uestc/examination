#! D:\pythoncode
# encoding: utf-8
"""
@author: longkun
@contact: 1256904448@qq.com
@software: pycharm
@file: 柱状图中的最大矩形.py
@time: 2020/2/2 17:28
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    x = [2, 1, 5, 6, 2, 3]
    a = s.largestRectangleArea(x)
    print(a)
