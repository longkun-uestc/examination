from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            print(stack, max_area)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                max_area = max(max_area, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    # heights = [5,5,5,5,5,5,5]
    # heights = [2,1,2]
    s = Solution()
    r = s.largestRectangleArea(heights)
    print(r)
