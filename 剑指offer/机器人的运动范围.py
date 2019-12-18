def compute(num):
    count = 0
    while num > 0:
        count += num % 10
        num = num // 10
    # print(count)
    return count


def check(n1, n2, threshold):
    return True if compute(n1) + compute(n2) <= threshold else False


class Solution:
    def movingCount(self, threshold, rows, cols):
        if threshold < 0:
            return 0
        stack = [(0, 0)]
        mask = [[0] * cols for i in range(rows)]
        # print(mask)
        mask[0][0] = 1
        while stack:
            i, j = stack.pop()
            if (0 <= i + 1 < rows) and mask[i + 1][j] == 0 and check(i + 1, j, threshold):
                stack.append((i + 1, j))
                mask[i + 1][j] = 1
            if (0 <= j + 1 < cols) and mask[i][j + 1] == 0 and check(i, j + 1, threshold):
                stack.append((i, j + 1))
                mask[i][j + 1] = 1
        count = 0
        for m in mask:
            print(m)
            count += m.count(1)
        print(count)
        return count


if __name__ == '__main__':
    # compute(132)
    s = Solution()
    s.movingCount(18, 40, 40)
