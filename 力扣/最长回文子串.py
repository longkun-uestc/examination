#! D:\pythoncode
# encoding: utf-8
"""
@author: longkun
@contact: 1256904448@qq.com
@software: pycharm
@file: 最长回文子串.py
@time: 2020/2/1 15:01
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        M = [[0 for i in range(len(s))] for j in range(len(s))]
        max_l = 0
        max_s = ""
        for i in range(len(s)):
            M[i][i] = 1
            max_s = s[i]
            max_l = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                M[i][i+1] = 2
                max_l = 2
                max_s = s[i:i+2]
        for r in range(3, len(s)+1):
            for i in range(len(s)-r+1):
                j = i+r-1
                if s[i] == s[j]:
                    if M[i+1][j-1] > 0:
                        M[i][j] = M[i+1][j-1] + 2
                        if M[i][j] > max_l:
                            max_s = s[i:j+1]
                            max_l = M[i][j]
        for m in M:
            print(m)
        print(max_s)
        return max_s

if __name__ == '__main__':
    s = Solution()
    x = "babad"
    # x = "abaaaaaaa"
    # x = "abcdcbaaa"
    x = "cbbd"
    x = "jhgtrclvzumufurdemsogfkpzcwgyepdwucnxrsubrxadnenhvjyglxnhowncsubvdtftccomjufwhjupcuuvelblcdnuchuppqpcujernplvmombpdttfjowcujvxknzbwmdedjydxvwykbbamfnsyzcozlixdgoliddoejurusnrcdbqkfdxsoxxzlhgyiprujvvwgqlzredkwahexewlnvqcwfyahjpeiucnhsdhnxtgizgpqphunlgikogmsffexaeftzhblpdxrxgsmeascmqngmwbotycbjmwrngemxpfakrwcdndanouyhnnrygvntrhcuxgvpgjafijlrewfhqrguwhdepwlxvrakyqgstoyruyzohlvvdhvqmzdsnbtlwctetwyrhhktkhhobsojiyuydknvtxmjewvssegrtmshxuvzcbrabntjqulxkjazrsgbpqnrsxqflvbvzywzetrmoydodrrhnhdzlajzvnkrcylkfmsdode"
    s.longestPalindrome(x)