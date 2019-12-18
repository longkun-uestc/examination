class Solution:
    count = [0, 1, 2]  # count[n] = count[n-1]+count[n-2]+...+count[2]+count[n-(n-1)]+1
    def jumpFloorII(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        for i in range(3, number + 1):
            self.count.append(sum(self.count)+1)
        return self.count[number]

if __name__ == '__main__':
    s = Solution()
    a = s.jumpFloorII(5)
    print(a)

