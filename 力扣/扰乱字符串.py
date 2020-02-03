#! D:\pythoncode
# encoding: utf-8
"""
@author: longkun
@contact: 1256904448@qq.com
@software: pycharm
@file: 扰乱字符串.py
@time: 2020/2/3 15:59
"""


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 and len(s2) == 0:
            return True
        if len(s1) == 1 and len(s2) == 1 and s1 == s2:
            return True
        a = sorted(s1)
        b = sorted(s2)
        if a == b:
            for i in range(1, len(s1)):
                res1 = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
                res2 = self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
                flag = res1 or res2
                if flag:
                    return flag
            return False
        else:
            return False

    def isScramble1(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 and len(s2) == 0:
            return True
        dp = [[[False for i in range(len(s1))] for j in range(len(s1))] for k in range(len(s1) + 1)]
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    dp[1][i][j] = True
        for k in range(2, len(s1) + 1):
            for i in range(len(s1) - k + 1):
                for j in range(len(s2) - k + 1):
                    res = False
                    for h in range(1, k):
                        r1 = dp[h][i][j] and dp[k - h][i + h][j + h]
                        r2 = dp[h][i][j + k - h] and dp[k - h][i + h][j]
                        if r1 or r2:
                            res = True
                            break
                    dp[k][i][j] = res
        for d in dp:
            print(d)
        return dp[len(s1)][0][0]


if __name__ == '__main__':
    s = Solution()
    a = 'great'
    b = "eatrg"
    a = "abcde"
    b = "caebd"
    c = s.isScramble1(a, b)
    print(c)


def isScramble1(self, s1: str, s2: str) -> bool:
    if len(s1) == 0 and len(s2) == 0:
        return True
    dp = [[[False for i in range(len(s1))] for j in range(len(s1))] for k in range(len(s1) + 1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[1][i][j] = True
    for k in range(2, len(s1) + 1):
        for i in range(len(s1) - k + 1):
            for j in range(len(s2) - k + 1):
                res = False
                for h in range(1, k):
                    r1 = dp[h][i][j] and dp[k - h][i + h][j + h]
                    r2 = dp[h][i][j + k - h] and dp[k - h][i + h][j]
                    if r1 or r2:
                        res = True
                        break
                dp[k][i][j] = res
    for d in dp:
        print(d)
    return dp[len(s1)][0][0]
