from typing import List


def check_visit(visit):
    for i in range(len(visit)):
        for j in range(len(visit[0])):
            if visit[i][j] == 0:
                return False
    return True


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        end = None
        visit = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] == 2:
                    end = (i, j)
                if grid[i][j] == -1:
                    visit[i][j] = 1
        visit[start[0]][start[1]] = 1
        q = [([start], visit)]
        count = 0
        while q:
            path, visited = q.pop(0)
            x, y = path[-1]
            if grid[x][y] == 2 and check_visit(visited):
                count += 1
            else:
                if (0 <= x + 1 < len(grid)) and grid[x + 1][y] != -1 and visited[x + 1][y] == 0:
                    new_visit = [v[:] for v in visited]
                    new_visit[x + 1][y] = 1
                    new_path = [p for p in path]
                    new_path.append((x + 1, y))
                    q.append((new_path, new_visit))
                if (0 <= x - 1 < len(grid)) and grid[x - 1][y] != -1 and visited[x - 1][y] == 0:
                    new_visit = [v[:] for v in visited]
                    new_visit[x - 1][y] = 1
                    new_path = [p for p in path]
                    new_path.append((x - 1, y))
                    q.append((new_path, new_visit))
                if (0 <= y + 1 < len(grid[0])) and grid[x][y + 1] != -1 and visited[x][y + 1] == 0:
                    new_visit = [v[:] for v in visited]
                    new_visit[x][y + 1] = 1
                    new_path = [p for p in path]
                    new_path.append((x, y + 1))
                    q.append((new_path, new_visit))
                if (0 <= y - 1 < len(grid[0])) and grid[x][y - 1] != -1 and visited[x][y - 1] == 0:
                    new_visit = [v[:] for v in visited]
                    new_visit[x][y - 1] = 1
                    new_path = [p for p in path]
                    new_path.append((x, y - 1))
                    q.append((new_path, new_visit))
        print(count)
        return count


if __name__ == '__main__':
    s = Solution()
    x =[[0,1],[2,0]]
    s.uniquePathsIII(x)
