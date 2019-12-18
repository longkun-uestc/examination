class Solution:  # 注意除去空格和越界问题
    def StrToInt(self, s):
        if len(s) == 0:
            return 0
        s = s.strip()
        symbol = 0
        if s[0] == "+":
            symbol = 0
            s = s[1:]
        elif s[0] == "-":
            symbol = 1
            s = s[1:]
        elif s[0] < "0" or s[0] > "9":
            return 0
        num = 0
        now = 1
        for i in range(len(s) - 1, -1, -1):
            if "0" <= s[i] <= "9":
                num += now * int(s[i])
                now *= 10
            else:
                return 0
        num = num if symbol == 0 else -num
        if num > 2**31-1 or num < -2**31:
            return 0
        return num


if __name__ == '__main__':
    s = Solution()
    a = s.StrToInt("-123")
    print(a)
