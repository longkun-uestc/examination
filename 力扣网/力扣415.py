class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        res_list = ["0" for i in range(max(i, j) + 2)]
        k = len(res_list) - 1
        cnt = 0
        while i >= 0 and j >= 0:
            n = (ord(num1[i]) - ord('0')) + (ord(num2[j]) - ord('0')) + cnt
            cnt = n // 10
            n = n % 10
            res_list[k] = str(n)
            k -= 1
            i -= 1
            j -= 1
        while i >= 0:
            n = ord(num1[i]) - ord('0') + cnt
            cnt = n // 10
            n = n % 10
            res_list[k] = str(n)
            k -= 1
            i -= 1
        while j >= 0:
            n = ord(num2[j]) - ord('0') + cnt
            cnt = n // 10
            n = n % 10
            res_list[k] = str(n)
            k -= 1
            j -= 1
        if cnt > 0:
            res_list[0] = str(cnt)
        if res_list[0] == -1:
            res = ''.join(res_list[1:])
        else:
            res = ''.join(res_list)
        return res


if __name__ == '__main__':
    s1 = '100'
    s2 = '5000000000'
    s1 = '99999999999999991111'
    s2 = '9111'
    a = Solution()
    a.addStrings(s1, s2)
