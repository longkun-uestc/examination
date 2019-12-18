# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.count = [0, 1, 2]  # count[n] = count[n-1]+count[n-2] 每次可以选择跳一阶或者两阶

    def jumpFloor(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        for i in range(3, number + 1):
            self.count.append(self.count[i - 1] + self.count[i - 2])
        return self.count[number]


if __name__ == '__main__':
    s = Solution()
    a = s.jumpFloor(5)
    print("-----")
    print(a)
