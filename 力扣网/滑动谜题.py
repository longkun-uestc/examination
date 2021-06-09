from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        row, col = len(board), len(board[0])
        x = []
        for i in range(row):
            for j in range(col):
                x.append(board[i][j])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = [(x, 0)]
        visited = set()
        while q:
            now, step = q.pop(0)
            print(now)
            if now == [1, 2, 3, 4, 5, 0]:
                return step
            if tuple(now) not in visited:
                visited.add(tuple(now))
                zero_ids = now.index(0)
                x, y = divmod(zero_ids, col)
                for d in directions:
                    tmp_x = x + d[0]
                    tmp_y = y + d[1]
                    if 0 <= tmp_x < row and 0 <= tmp_y < col:
                        tmp = now[:]
                        tmp[x * col + y] = tmp[tmp_x * col + tmp_y]
                        tmp[tmp_x * col + tmp_y] = 0
                        q.append((tmp, step + 1))
        return -1


if __name__ == '__main__':
    s = Solution()
    a = s.slidingPuzzle([[3, 2, 4], [1, 5, 0]])
    print(a)
