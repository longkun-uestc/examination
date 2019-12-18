class Solution:
    def rectCover(self, number):
        if number < 1:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        first = 1
        second = 2
        for i in range(3, number+1):
            result = first + second
            first = second
            second = result
        return result


if __name__ == '__main__':
    s = Solution()
    a = s.rectCover(4)
    print(a)
