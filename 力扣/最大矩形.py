#! D:\pythoncode
# encoding: utf-8
"""
@author: longkun
@contact: 1256904448@qq.com
@software: pycharm
@file: 最大矩形.py
@time: 2020/2/2 14:24
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        heights = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix[0])):
            if matrix[0][i] == "1":
                heights[0][i] = 1
        max_area = 0
        max_area = max(max_area, self.largestRectangleArea(heights[0]))
        for i in range(1, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[i][j] = heights[i-1][j] + 1
            max_area = max(max_area, self.largestRectangleArea(heights[i]))
        print(max_area)
        return max_area

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
    x = [
        ["1", "0", "1", "0", "0", "1"],
        ["1", "0", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "1", "1"]
    ]
    # x = [["0", "1", "1", "0", "1"],
    #      ["1", "1", "0", "1", "0"],
    #      ["0", "1", "1", "1", "0"],
    #      ["1", "1", "1", "1", "0"],
    #      ["1", "1", "1", "1", "1"],
    #      ["0", "0", "0", "0", "0"]]
    s.maximalRectangle(x)
