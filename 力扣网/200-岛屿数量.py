from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c, index):
            grid[r][c] = index
            neighbor = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for nr, nc in neighbor:
                if 0 <= r + nr < len(grid) and 0 <= c + nc < len(grid[0]) and grid[r + nr][c + nc] == "1":
                    dfs(r + nr, c + nc, index)

        index = 2
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j, index)
                    index += 1
                    count += 1
        return count


if __name__ == '__main__':
    g = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]
    s = Solution()
    r = s.numIslands(grid=g)
    print(r)
