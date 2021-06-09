import math


def check(N):
    if N == 1:
        return False
    if N == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True


class Solution:
    def primePalindrome(self, N: int) -> int:
        str_n = str(N)
        ids = math.ceil(len(str_n) / 2)
        print(str_n, ids)
        root = str_n[:ids]
        i = 0
        num = []
        while True:
            n1 = int(root + root[:-1][::-1])
            n2 = int(root + root[::-1])
            print(n1, n2)
            if n1 >= N and check(n1):
                num.append(n1)
            if n2 >= N and check(n2):
                num.append(n2)
            if root == root[::-1]:
                n3 = int(root)
                if n3 >= N and check(n3):
                    num.append(n3)
            root = str(int(root) + 1)
            i = i + 1
            if i % 10 == 0 and len(num) > 0:
                return min(num)


if __name__ == '__main__':
    s = Solution()
    a = s.primePalindrome(2)
    print(a)
