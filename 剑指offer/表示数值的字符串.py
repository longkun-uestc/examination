class Solution:
    # s字符串
    def isNumeric(self, s):
        if len(s) == 0:
            return False
        if s[0] == "+" or s[0] == "-":
            s = s[1:]
        elif (s[0] < "0" or s[0] > "9") and s[0] != ".":
            return False
        if (s[0] < "0" or s[0] > "9") and s[0] != ".":
            return False
        if s[0] == ".":
            s = s[1:]
            flag1 = False
        else:
            flag1 = True
        flag2 = True
        print(s)
        for ids in range(1, len(s)):
            if (s[ids] < "0" or s[ids] > "9") and s[ids] != "+" and s[ids] != "-" and s[ids] != 'e' and s[ids] != "E" and s[ids] != ".":
                return False
            if s[ids] == ".":  # 判断小数点
                if not flag2:
                    print("e后面的小数点")
                    return False
                if flag1:
                    flag1 = False
                else:
                    return False
            if s[ids] == "e" or s[ids] == "E":  # 判断科学计数法
                if ids == len(s) - 1:
                    return False
                if flag2:
                    flag2 = False
                else:
                    return False
            if (s[ids] == "+" or s[ids] == "-") and s[ids - 1] != "e" and s[ids - 1] != "E":  # 判断科学计数法后面的符号
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    a = s.isNumeric("00100")
    print(a)

