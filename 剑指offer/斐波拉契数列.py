# -*- coding:utf-8 -*-
import numpy as np


class Solution:
    def __init__(self):
        self.table = np.zeros(40, dtype=np.int32) - 1
        self.table[0] = 0
        self.table[1] = 1

    def Fibonacci(self, n):
        if n <= 1:
            return self.table[n]
        else:
            for i in range(2, n + 1):
                self.table[i] = self.table[i - 2] + self.table[i - 1]
            print(self.table)
            print(self.table.shape)
            return self.table[n]


if __name__ == '__main__':
    s = Solution()
    a = s.Fibonacci(39)
    print(a)
