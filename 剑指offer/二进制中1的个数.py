class Solution:
    def NumberOf1(self, n):
        if n == 0:
            return 0
        if n > 0:
            count = 0
            while n > 0:
                y = n % 2
                if y == 1:
                    count += 1
                n = n // 2
            return count
        elif n < 0:
            binary = [0] * 32
            n = -n
            ids = 0
            while n > 0:
                y = n % 2
                binary[ids] = y
                ids += 1
                n = n // 2
            ids = binary.index(1)
            count = binary[ids + 1:].count(0)
            count += 1
            return count

def good_NumberOf1(self, n):
    # 优秀解法
    # 首先bin()函数可以将整数转换为2进制，例如bin(4)='0b100'， bin(-4) = '-0b100'
    # 对负数，bin(还是用原码表示输出的)。此时要想输出负数补码的1的个数，就要将补码转换为原码
    # 计算机表示有符号整数时，范围是[-2**32, 2**32-1]，用补码表示的
    # 将补码加上2**32就等价于把有符号数转换成了无符号数,考虑溢出，此时范围成了[0, 2*33-1]
    # 其次，负数的补码加上2**32就等价于将其转换成了原码，再直接数1就可以了。
    # 例如-3的补码表示为：1101。将其加上2**3，等于1101+1000=10101
    return bin(n).replace("0b", "").count("1") if n >= 0 else bin(2 ** 32 + n).replace("0b", "").count("1")

if __name__ == '__main__':
    s = Solution()
    a = s.NumberOf1(-2)
    print(a)
