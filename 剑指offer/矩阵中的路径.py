class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(path) > rows * cols or rows * cols == 0 or len(path) == 0:
            return False
        # if len(matrix) == 1 and len(path) == 1 and matrix == path:
        #     return True
        matrix = [matrix[i * cols: (i+1)*cols] for i in range(rows)]
        matrix = [list(m) for m in matrix]
        mask = [[0] * cols for i in range(rows)]
        start = []
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == path[0]:
                    start.append((i, j))
        if len(start) == 0:
            return False
        for p in start:
            stack = [p]
            mask[p[0]][p[1]] = 1
            path_ids = 1
            while stack:
                if path_ids == len(path):
                    return True
                i, j = stack[-1]
                if (0 <= j - 1 < cols) and mask[i][j - 1] == 0 and matrix[i][j - 1] == path[path_ids]:
                    stack.append((i, j - 1))
                    mask[i][j - 1] = 1
                    path_ids += 1
                elif (0 <= j + 1 < cols) and mask[i][j + 1] == 0 and matrix[i][j + 1] == path[path_ids]:
                    stack.append((i, j + 1))
                    mask[i][j + 1] = 1
                    path_ids += 1
                elif (0 <= i - 1 < rows) and mask[i - 1][j] == 0 and matrix[i - 1][j] == path[path_ids]:
                    stack.append((i - 1, j))
                    mask[i - 1][j] = 1
                    path_ids += 1
                elif (0 <= i + 1 < rows) and mask[i + 1][j] == 0 and matrix[i + 1][j] == path[path_ids]:
                    stack.append((i + 1, j))
                    mask[i + 1][j] = 1
                    path_ids += 1
                else:
                    if (0 <= i + 1 < rows) and mask[i + 1][j] == 2:
                        mask[i + 1][j] = 0
                    if (0 <= i - 1 < rows) and mask[i - 1][j] == 2:
                        mask[i - 1][j] = 0
                    if (0 <= j + 1 < cols) and mask[i][j + 1] == 2:
                        mask[i][j + 1] = 0
                    if (0 <= j - 1 < cols) and mask[i][j - 1] == 2:
                        mask[i][j - 1] = 0
                    mask[i][j] = 2
                    stack.pop()
                    path_ids -= 1
            mask = [[0] * cols for i in range(rows)]
        return False


if __name__ == '__main__':
    # matrix = [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]
    # path = "abcb"
    # matrix = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    matrix = "ABCESFCSADEE"
    matrix = "A"
    path = "A"
    rows = 1
    cols = 1
    s = Solution()
    a = s.hasPath(matrix, rows, cols, path)
    print(a)
