class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        directions = ["R", "B", "L", "T"]
        r_start = 0
        r_end = len(matrix) - 1
        c_start = 0
        c_end = len(matrix[0]) - 1
        flag = 0
        result = []
        while r_start <= r_end and c_start <= c_end:
            direction = directions[flag % 4]
            if direction == "R":
                for i in range(c_start, c_end + 1):
                    result.append(matrix[r_start][i])
                r_start += 1
            elif direction == "B":
                for i in range(r_start, r_end + 1):
                    result.append(matrix[i][c_end])
                c_end -= 1
            elif direction == "L":
                for i in range(c_end, c_start - 1, -1):
                    result.append(matrix[r_end][i])
                r_end -= 1
            else:
                for i in range(r_end, r_start - 1, -1):
                    result.append(matrix[i][c_start])
                c_start += 1
            flag += 1
        return result


if __name__ == '__main__':
    x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    x = [[1,2,3,4,5,6]]
    x= [[1],[2],[3],[4]]
    # for i in range(4, -1, -1):
    #     print(i)
    # exit()
    s = Solution()
    a = s.printMatrix(x)
    print(a)
