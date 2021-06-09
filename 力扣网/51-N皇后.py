from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["".join(['.' for i in range(n)]) for j in range(n)]
        visited = [[0 for i in range(n)] for j in range(n)]
        self.all = []
        def check(board, visited, n):
            if n >= len(board):
                self.all.append(board[:])
                return
            for i in range(len(board)):
                if visited[n][i] == 0:
                    check_board = board[:]
                    check_visited = [v[:] for v in visited]
                    tmp = check_board[n]
                    tmp = tmp[:i] + "Q" + tmp[i+1:]
                    check_board[n] = tmp
                    solve_visited(check_visited, n, i)
                    check(check_board, check_visited, n+1)

        def solve_visited(visited, x, y):
            for i in range(len(visited)):
                visited[x][i] = 1
                visited[i][y] = 1
                if x-i >= 0 and y-i >= 0:
                    visited[x-i][y-i] = 1
                if x-i >= 0 and y+i < len(visited):
                    visited[x-i][y+i] = 1
                if x+i < len(visited) and y-i >= 0:
                    visited[x+i][y-i] = 1
                if x+i < len(visited) and y+i < len(visited):
                    visited[x+i][y+i] = 1

        check(board, visited, 0)
        # for i, al in enumerate(self.all):
        #     print(i)
        #     for a in al:
        #         print(a)

        return self.all


if __name__ == '__main__':
    s = Solution()
    s.solveNQueens(8)