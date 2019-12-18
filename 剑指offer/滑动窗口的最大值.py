class Solution:
    def maxInWindows(self, num, size):
        if len(num) < size or size < 1:
            return []
        result = []
        for i in range(len(num)-size + 1):
            print(i, num[i: i + size])
            result.append(max(num[i:i + size]))
        print(result)
        return result

if __name__ == '__main__':
    x = [2,3,4,2,6,2,5,1]
    s = Solution()
    s.maxInWindows(x, 3)
