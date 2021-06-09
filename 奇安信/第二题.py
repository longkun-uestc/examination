class Solution:
    def house(self, person):
        if len(person) < 2:
            return len(person)
        arr = [1] * len(person)
        i = 1
        while i < len(person):
            if person[i] > person[i-1]:
                arr[i] = arr[i-1] + 1
            i += 1
        i = len(person) - 2
        while i >= 0:
            if person[i] > person[i+1]:
                arr[i] = max(arr[i], arr[i+1] + 1)
            i -= 1
        print(arr)
        return sum(arr)
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
