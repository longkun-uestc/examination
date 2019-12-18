class Solution:
    def Add(self, num1, num2):
        if num2 == 0:
            return num1
        sum = 0
        carry = 0
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum & 0xFFFFFFFF # 考虑负数
            num2 = carry
            # print(bin(num1), bin(num2))
        num1 = num1 if num1 >> 31 == 0 else num1 - 4294967296
        # print(num1)
        return num1


if __name__ == '__main__':
    s = Solution()
    s.Add(-3, 5)
