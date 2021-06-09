from typing import List


def to_tuple(mat):
    result = []
    for m in mat:
        result.extend(m)
    return tuple(result)


def flip(mat, x, y):
    m = [row[:] for row in mat]
    m[x][y] = m[x][y] ^ 1
    if 0 <= x + 1 < len(m):
        m[x + 1][y] = m[x + 1][y] ^ 1
    if 0 <= x - 1 < len(m):
        m[x - 1][y] = m[x - 1][y] ^ 1
    if 0 <= y + 1 < len(m[0]):
        m[x][y + 1] = m[x][y + 1] ^ 1
    if 0 <= y - 1 < len(m[0]):
        m[x][y - 1] = m[x][y - 1] ^ 1
    return m


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        if len(mat) == 1 and len(mat[0]) == 1 and mat[0][0] == 0:
            return 0
        if len(mat) == 1 and len(mat[0]) == 1 and mat[0][0] == 1:
            return 1
        ends = to_tuple([[0 for i in range(len(mat[0]))] for j in range(len(mat))])
        visited = set()
        q = [(mat, 0)]
        while q:
            m, step = q.pop(0)
            tuple_m = to_tuple(m)
            if tuple_m == ends:
                return step
            if tuple_m not in visited:
                for i in range(len(m)):
                    for j in range(len(m[0])):
                        flip_m = flip(m, i, j)
                        q.append((flip_m, step + 1))
                visited.add(tuple_m)
        return -1


if __name__ == '__main__':
    s = Solution()
    x = [[0, 0], [0, 1]]
    x = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    x = [[1,0,0],[1,0,0]]
    # for a in x:
    #     print(a)
    # print("------------------")
    # y = flip(x, 1, 1)
    # for a in y:
    #     print(a)
    # exit()
    a = s.minFlips(x)
    print(a)
