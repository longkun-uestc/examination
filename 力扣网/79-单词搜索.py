from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, visited, word, x, y):
            if not word:
                return True
            if board[x][y] == word[0]:
                visited[x][y] = True
                if len(word) == 1:
                    return True
                move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                flag = False
                for mv in move:
                    x1 = x + mv[0]
                    y1 = y + mv[1]
                    if 0 <= x1 < len(board) and 0 <= y1 < len(board[0]) and not visited[x1][y1]:
                        flag = dfs(board, visited, word[1:], x1, y1) or flag
                if not flag:
                    visited[x][y] = False
                return flag
            else:
                return False

        if not word:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = [[False for __ in range(len(board[0]))] for _ in range(len(board))]
                    if dfs(board, visited, word, i, j): return True
        return False
if __name__ == '__main__':
    s = Solution()
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    word = "SEE"
    word = "ABCB"
    res = s.exist(board, word)
    print(res)