from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        stack = [[sr, sc]]
        search = [[False for i in range(len(image[0]))] for j in range(len(image))]
        color = image[sr][sc]
        while stack:
            n_sr, n_sc = stack.pop()
            image[n_sr][n_sc] = newColor
            search[n_sr][n_sc] = True
            if n_sr - 1 >= 0 and image[n_sr-1][n_sc] == color and not search[n_sr-1][n_sc]:
                stack.append([n_sr-1, n_sc])
            if n_sr + 1 < len(image) and image[n_sr+1][n_sc] == color and not search[n_sr+1][n_sc]:
                stack.append([n_sr+1, n_sc])
            if n_sc - 1 >= 0 and image[n_sr][n_sc-1] == color and not search[n_sr][n_sc-1]:
                stack.append([n_sr, n_sc-1])
            if n_sc + 1 < len(image[0]) and image[n_sr][n_sc+1] == color and not search[n_sr][n_sc+1]:
                stack.append([n_sr, n_sc+1])
        return image

