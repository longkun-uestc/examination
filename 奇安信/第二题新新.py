class Solution:
    def house(self, person):
        left = [1 for _ in range(len(person))]
        right = left[:]
        for i in range(1, len(person)):
            if person[i] > person[i - 1]:
                left[i] = left[i - 1] + 1
        count = left[-1]
        for i in range(len(person) - 2, -1, -1):
            if person[i] > person[i+1]:
                right[i] = right[i+1] + 1
            count += max(left[i], right[i])
        return count
if __name__ == '__main__':
    s = Solution()
    p = [4, 1, 3, 3, 3]
    p = [3, 2, 4]
    p = [1]
    p = [2,2,2,2,1,2,3,4,4,4,3,2,2,3,4,5,5,5,4,3,2,1,1,1,1]
    # p = [2,2,2,2,2]
    # p = [1,2,3,2,1]
    r = s.house(p)
    print(r)