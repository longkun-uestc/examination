from typing import List


def change_visited(is_visited, x, y):
    for i in range(len(is_visited)):
        is_visited[x][i] = 1
        is_visited[i][y] = 1
        if 0<=x-y+i<len(is_visited):
            is_visited[x-y+i][i] = 1
        if 0<=x+y-i<len(is_visited):
            is_visited[x+y-i][i] = 1


def check(checkerboard, is_visited, n, all):
    if n >= len(checkerboard):
        all.append(checkerboard)
        return
    for i in range(len(checkerboard)):
        if is_visited[n][i] == 0:
            board = checkerboard[:]
            visited = [v[:] for v in is_visited]
            tmp = list(board[n])
            tmp[i] = "Q"
            board[n] = "".join(tmp)
            change_visited(visited, n, i)
            # for b in board:
            #     print(b)
            # for v in visited:
            #     print(v)
            # print("----------------------------")
            check(board, visited, n+1, all)





class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        checkboard = ["".join(["." for i in range(n)]) for j in range(n)]
        is_visited = [[0 for j in range(n)] for i in range(n)]
        all = []
        check(checkboard, is_visited, 0, all)
        print(all)
        for i, a in enumerate(all):
            for j, b in enumerate(a):
               print(b)
            print("----------------")
        print(len(all))
        return all


if __name__ == '__main__':
    # x = [[0 for j in range(8)] for i in range(8)]
    # change_visited(x, 3, 4)
    s = Solution()
    s.solveNQueens(12)



