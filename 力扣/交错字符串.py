#! D:\pythoncode
# encoding: utf-8
"""
@author: longkun
@contact: 1256904448@qq.com
@software: pycharm
@file: 交错字符串.py
@time: 2020/2/4 14:05
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # print(s1)
        # print(s2)
        # print(s3)
        # print("---------------------------------------")
        print(len(s1), len(s2), len(s3))
        if s1 == s3 and len(s2) == 0:
            return True
        if s2 == s3 and len(s1) == 0:
            return True
        # if (len(s1) + len(s2)) != len(s3):
        #     return False
        if len(s1) > 0 and len(s2) > 0 and len(s3) > 0:
            if s1[-1] != s3[-1] and s2[-1] != s3[-1]:
                return False
            elif s1[-1] == s3[-1] and s2[-1] != s3[-1]:
                return self.isInterleave(s1[:-1], s2, s3[:-1])
            elif s1[-1] != s3[-1] and s2[-1] == s3[-1]:
                return self.isInterleave(s1, s2[:-1], s3[:-1])
            else:
                return self.isInterleave(s1[:-1], s2, s3[:-1]) or self.isInterleave(s1, s2[:-1], s3[:-1])
        return False

    def isInterleave1(self, s1: str, s2: str, s3: str) -> bool:
        # if len(s1) + len(s2) != len(s3):
        #     return False
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
        dp = [[[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] for k in range(len(s3) + 1)]
        dp[0][0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][i][0] = dp[i - 1][i - 1][0]
        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[j][0][j] = dp[j - 1][0][j - 1]

        for k in range(2, len(s3) + 1):
            for i in range(1, min(len(s1) + 1, k)):
                j = k - i
                if j <= len(s2):
                    if s1[i - 1] == s3[k - 1] and s2[j - 1] == s3[k - 1]:
                        dp[k][i][j] = dp[k - 1][i - 1][j] or dp[k - 1][i][j - 1]
                    elif s1[i - 1] == s3[k - 1] and s2[j - 1] != s3[k - 1]:
                        dp[k][i][j] = dp[k - 1][i - 1][j]
                    elif s1[i - 1] != s3[k - 1] and s2[j - 1] == s3[k - 1]:
                        dp[k][i][j] = dp[k - 1][i][j - 1]
                    else:
                        dp[k][i][j] = False

        # for i, ap in enumerate(dp[:5]):
        #     print("------------", i)
        #     for bp in ap:
        #         print(bp)

        return dp[len(s3)][len(s1)][len(s2)]


if __name__ == '__main__':
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    s1 = "ab"
    s2 = "bc"
    s3 = "bbac"
    s1 = "baababbabbababbaaababbbbbbbbbbbaabaabaaaabaaabbaaabaaaababaabaaabaabbbbaabbaabaabbbbabbbababbaaaabab"
    s2 = "aababaaabbbababababaabbbababaababbababbbbabbbbbababbbabaaaaabaaabbabbaaabbababbaaaababaababbbbabbbbb"
    s3 = "babbabbabbababbaaababbbbaababbaabbbbabbbbbaaabbabaababaabaaabaabbbaaaabbabbaaaaabbabbaabaaaabbbbababbbababbabaabababbababaaaaaabbababaaabbaabbbbaaaaabbbaaabbbabbbbaaabaababbaabababbbbababbaaabbbabbbab"
    # s1 = "aaaaa"
    # s2 = "bbbbb"
    # s3 = "aababababb"
    # s1 = "a"
    # s2 = ""
    # s3 = "aa"
    a = s.isInterleave(s1, s2, s3)
    print(a)


def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
        return True
    dp = [[[False for i in range(len(s2) + 1)] for j in range(len(s1) + 1)] for k in range(len(s3) + 1)]
    dp[0][0][0] = True
    for i in range(1, len(s1) + 1):
        if s1[i - 1] == s3[i - 1]:
            dp[i][i][0] = dp[i - 1][i - 1][0]
    for j in range(1, len(s2) + 1):
        if s2[j - 1] == s3[j - 1]:
            dp[j][0][j] = dp[j - 1][0][j - 1]

    for k in range(2, len(s3) + 1):
        for i in range(1, min(len(s1) + 1, k)):
            j = k - i
            if j <= len(s2):
                if s1[i - 1] == s3[k - 1] and s2[j - 1] == s3[k - 1]:
                    dp[k][i][j] = dp[k - 1][i - 1][j] or dp[k - 1][i][j - 1]
                elif s1[i - 1] == s3[k - 1] and s2[j - 1] != s3[k - 1]:
                    dp[k][i][j] = dp[k - 1][i - 1][j]
                elif s1[i - 1] != s3[k - 1] and s2[j - 1] == s3[k - 1]:
                    dp[k][i][j] = dp[k - 1][i][j - 1]
                else:
                    dp[k][i][j] = False

    return dp[len(s3)][len(s1)][len(s2)]
