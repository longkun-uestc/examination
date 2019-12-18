class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(n+1):
            count += list(str(i)).count("1")
        return count

if __name__ == '__main__':
    s = Solution()
    a = s.NumberOf1Between1AndN_Solution(13)
    print(a)