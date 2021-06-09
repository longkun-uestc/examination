from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        stack = [click]
        search = set()
        while stack:
            now = stack.pop(0)
            pos, count = self.get_pos(board, now)
            board[now[0]][now[1]] = str(count) if count > 0 else 'B'
            if count == 0:
                for p in pos:
                    if tuple(p) not in search and p not in stack:
                        stack.append(p)
            search.add(tuple(now))
        for b in board:
            print(b)
        return board

    def get_pos(self, board, click):
        count = 0
        pos = []
        if click[0] - 1 >= 0:
            if board[click[0] - 1][click[1]] != 'M':
                pos.append([click[0] - 1, click[1]])
            else:
                count += 1
        if click[0] + 1 < len(board):
            if board[click[0] + 1][click[1]] != 'M':
                pos.append([click[0] + 1, click[1]])
            else:
                count += 1
        if click[1] - 1 >= 0:
            if board[click[0]][click[1] - 1] != 'M':
                pos.append([click[0], click[1] - 1])
            else:
                count += 1
        if click[1] + 1 < len(board[0]):
            if board[click[0]][click[1] + 1] != 'M':
                pos.append([click[0], click[1] + 1])
            else:
                count += 1
        if click[0] - 1 >= 0 and click[1] - 1 >= 0:
            if board[click[0] - 1][click[1] - 1] != 'M':
                pos.append([click[0]-1, click[1]-1])
            else:
                count += 1
        if click[0] - 1 >= 0 and click[1] + 1 < len(board[0]):
            if board[click[0]-1][click[1]+1] != 'M':
                pos.append([click[0]-1, click[1]+1])
            else:
                count += 1
        if click[0] + 1 < len(board) and click[1] - 1 >= 0:
            if board[click[0]+1][click[1]-1] != 'M':
                pos.append([click[0]+1, click[1]-1])
            else:
                count += 1
        if click[0] + 1 < len(board) and click[1] + 1 < len(board[0]):
            if board[click[0]+1][click[1]+1] != 'M':
                pos.append([click[0]+1, click[1]+1])
            else:
                count += 1
        return pos, count


if __name__ == '__main__':
    s = Solution()
    board = [['E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'M', 'E', 'E'],
             ['E', 'E', 'E', 'M', 'E'],
             ['E', 'E', 'E', 'E', 'E']]
    click = [3, 0]
    s.updateBoard(board, click)
