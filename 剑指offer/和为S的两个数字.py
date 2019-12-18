class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) < 2:
            return []
        if len(array) == 2 and array[0] + array[1] != tsum:
            return []
        min_multiply = float('inf')
        now = float("inf")
        start, end = (0, len(array) - 1)
        while start < end:
            b = tsum - array[start]
            for i in range(end, start, -1):
                if b > array[i]:
                    end = i
                    break
                if b == array[i]:
                    mul = array[start] * b
                    if mul < min_multiply:
                        now = array[start]
                        min_multiply = mul
                    end = i
                    break
            start += 1
        if now == float("inf"):
            return []
        print([now, tsum - now])
        return [now, tsum - now]


if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 4, 7, 11, 15]
    import numpy as np

    x = list(np.arange(5, 1000))
    s.FindNumbersWithSum(x, 800)
