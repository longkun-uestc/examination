class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) == 0:
            return -1
        i = 0
        for i in range(len(s)):
            c = s.count(s[i])
            if c == 1:
                return i
        if i == len(s) - 1:
            return -1
