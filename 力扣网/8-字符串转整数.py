import re
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        if not s or s[0] < '0' and s[0] > '9' and s[0] != '+' and s[0] != '-':
            return 0
        if s[0] == '-':
            flag = s[0]
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
            flag = ''
        else:
            flag = ''
        i = 0
        while i < len(s) and '0' <= s[i] <= '9':
            i += 1
        s = s[:i]
        num = 0
        cnt = 1

        for i in range(len(s)-1, -1, -1):
            num += cnt * (ord(s[i]) - ord('0'))
            cnt *= 10
        if flag:
            num = -num
        if num < -2**31:
            num = -2**31
        if num > 2**31 - 1:
            num = 2**31-1
        return num

    def myAtoi1(self, str):
        str = str.strip()
        patten = r'^([+-]{0,1})(\d+)'
        res = re.search(patten, str)
        if res:
            flag = res.group(1)
            num = res.group(2)
            print(flag)
            print(num)
            num = int(num)
            if flag == '-':
                num = -num
            if num < -2 ** 31:
                num = -2 ** 31
            if num > 2 ** 31 - 1:
                num = 2 ** 31 - 1
            return num
        else:
            print(None)
            return 0

    def myAtoi2(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        # num.append('123')
        print(num)
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        print(num)
        return max(min(num,INT_MAX),INT_MIN)    #返回值


if __name__ == '__main__':
    s = Solution()
    x = "   -1234 word   "
    s.myAtoi2(x)


