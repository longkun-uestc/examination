from typing import List


class Unsolved:
    def __init__(self, location):
        self.num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.ids_list = []
        self.location = location

    def __len__(self):
        return len(self.num_list)

    def __repr__(self):
        s = self.location + " " + str(self.num_list) + str(self.ids_list)
        return s


def check(num, board, position):
    count = 0
    x, y = position
    flag = True
    for i in range(len(board[0])):
        if board[x][i] == num:
            flag = False
            break
    if flag:
        count += 1
    flag = True
    for i in range(len(board)):
        if board[i][y] == num:
            flag = False
            break
    if flag:
        count += 1
    flag = True
    binx, biny = (x // 3, y // 3)
    for i in range(3):
        for j in range(3):
            idsx, idsy = (binx * 3 + i, biny * 3 + j)
            if board[idsx][idsy] == num:
                flag = False
    if flag:
        count += 1
    # print(board[x])
    # for j in range(9):
    #     print(board[j][y], end=" ")
    # print()
    # for i in range(3):
    #     for j in range(3):
    #         idsx, idsy = (binx * 3 + i, biny * 3 + j)
    #         print(board[idsx][idsy], end=" ")
    #     print()
    # print(count)
    return True if count == 3 else False


def dfs(board, row, col, block, i, j):
    while board[i][j] != ".":
        j += 1
        if j >= len(board[0]):
            j = 0
            i += 1
        if i >= len(board):
            return True
    for n in range(len(board)):
        block_index = (i // 3) * 3 + j // 3
        if row[i][n] is False and col[j][n] is False and block[block_index][n] is False:
            board[i][j] = str(n + 1)
            row[i][n] = True
            col[j][n] = True
            block[block_index][n] = True
            if dfs(board, row, col, block, i, j):
                return True
            else:
                board[i][j] = "."
                row[i][n] = False
                col[j][n] = False
                block[block_index][n] = False
    return False



class Solution:
    def solveSudoku1(self, board: List[List[str]]) -> None:
        row = [[False for i in range(len(board[0]))] for j in range(len(board))]
        col = [[False for i in range(len(board[0]))] for j in range(len(board))]
        block = [[False for i in range(len(board[0]))] for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    row[i][num] = True
                    col[j][num] = True
                    pos = (i // 3) * 3 + j // 3
                    block[pos][num] = True
        dfs(board, row, col, block, 0, 0)
        for b in board:
            print(b)

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        all_unsolved = []

        for i in range(len(board)):
            unsolved = Unsolved(location="row{}".format(i))
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    unsolved.ids_list.append((i, j))
                else:
                    ids = unsolved.num_list.index(board[i][j])
                    unsolved.num_list.pop(ids)
            all_unsolved.append(unsolved)
        for j in range(len(board[0])):
            unsolved = Unsolved(location="col{}".format(j))
            for i in range(len(board)):
                if board[i][j] == ".":
                    unsolved.ids_list.append((i, j))
                else:
                    ids = unsolved.num_list.index(board[i][j])
                    unsolved.num_list.pop(ids)
            all_unsolved.append(unsolved)
        for i in range(len(board)):
            unsolved = Unsolved(location="bin{}".format(i))
            x1, y1 = divmod(i, 3)
            for j in range(len(board[0])):
                x2, y2 = divmod(j, 3)
                x, y = (x1 * 3 + x2, y1 * 3 + y2)
                if board[x][y] == ".":
                    unsolved.ids_list.append((x, y))
                else:
                    ids = unsolved.num_list.index(board[x][y])
                    unsolved.num_list.pop(ids)
            all_unsolved.append(unsolved)

        # all_unsolved.sort(key=lambda a: len(a))
        flag = True
        # while flag:
        for step in range(5):
            for i in range(len(all_unsolved)):
                unsolved = all_unsolved[i]
                print(unsolved)
                for num in unsolved.num_list:
                    count = 0
                    insert_ids = (-1, -1)
                    a, b = (0, '2')
                    for un_ids in unsolved.ids_list:
                        result = check(num, board, un_ids)
                        # if i == a and num == b:
                        #     print(result, num, un_ids)
                        if result:
                            count += 1
                            insert_ids = un_ids
                    # if i == a and num == b:
                    #     print(count, num)
                    #     exit()
                    if count == 1:
                        x, y = insert_ids
                        board[x][y] = num
                        print(i, "insert", insert_ids, num)
                        print(all_unsolved[x], all_unsolved[9 + y], all_unsolved[(x // 3) * 3 + y // 3 + 18])
                        all_unsolved[x].num_list.remove(num)
                        all_unsolved[x].ids_list.remove(insert_ids)
                        all_unsolved[9 + y].num_list.remove(num)
                        all_unsolved[9 + y].ids_list.remove(insert_ids)
                        all_unsolved[(x // 3) * 3 + y // 3 + 18].num_list.remove(num)
                        all_unsolved[(x // 3) * 3 + y // 3 + 18].ids_list.remove(insert_ids)
                        print(all_unsolved[x], all_unsolved[9 + y], all_unsolved[(x // 3) * 3 + y // 3 + 18])
                        print("------------------------------------------")
            flag = False
            for unsolve in all_unsolved:
                if len(unsolve) != 0:
                    flag = True
            print("step:", step, flag)
        for b in board:
            print(b)


if __name__ == '__main__':
    BOARD = [['5', '3', ".", ".", '7', ".", ".", '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    a = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", "2", ".", "1", ".", "9", ".", ".", "."],
         [".", ".", "7", ".", ".", ".", "2", "4", "."],
         [".", "6", "4", ".", "1", ".", "5", "9", "."],
         [".", "9", "8", ".", ".", ".", "3", ".", "."],
         [".", ".", ".", "8", ".", "3", ".", "2", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "6"],
         [".", ".", ".", "2", "7", "5", "9", ".", "."]]
    # a = Unsolved()
    # print(a)
    # exit()
    s = Solution()
    s.solveSudoku1(a)

    '''
    ValueError: '5' is not in list
Line 66 in solveSudoku (Solution.py)
Line 149 in _driver (Solution.py)
Line 163 in <module> (Solution.py)
    '''
