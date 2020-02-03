#! D:\pythoncode
# encoding: utf-8
"""
@author: longkun
@contact: 1256904448@qq.com
@software: pycharm
@file: 正则表达式匹配.py
@time: 2020/2/1 16:04
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        M = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        M[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j-1] == "*":
                M[0][j] = M[0][j-2]
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if s[i-1] == p[j-1] or p[j-1] == ".":
                    M[i][j] = M[i-1][j-1]
                elif p[j-1] == "*":
                    flag = M[i-1][j] if s[i-1] == p[j-2] or p[j-2] == "." else False
                    M[i][j] = M[i][j-2] or M[i][j-1] or flag
        for m in M:
            print(m)
        return M[len(s)][len(p)]

if __name__ == '__main__':
    solution = Solution()
    a = "ab"
    b = ".*"
    # a = "a"
    # b = "c*a"
    # a = "mississippi"
    # b = "mis*is*ip*."
    # a = "aab"
    # b = "c*a*b"
    r = solution.isMatch(a, b)
    print(r)