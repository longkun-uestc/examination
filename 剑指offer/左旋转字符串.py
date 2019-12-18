class Solution:
    def LeftRotateString(self, s, n):
        if len(s) == 0:
            return s
        n = n%len(s)
        s1 = s[:n]
        s2 = s[n:]
        return s2+s1


if __name__ == '__main__':
    s = Solution()
    x = 'asdfghjkf'
    a = s.LeftRotateString(x, 31)
    print(a)
