class Solution:
    def house(self, person):
        if len(person) < 2:
            return len(person)
        arr = [1] * len(person)
        i = 0
        while i < len(person) - 1:
            while i < len(person) - 1 and person[i] >= person[i + 1]:
                i += 1
            arr[i] = 1
            j = i + 1
            while j < len(person) and person[j] > person[j - 1]:
                arr[j] = arr[j - 1] + 1
                j += 1
            i = j
        i = len(person) - 1
        while i > 0:
            while i > 0 and person[i] >= person[i - 1]:
                i -= 1
            arr[i] = 1
            j = i - 1
            while j >= 0 and person[j] > person[j + 1]:
                arr[j] = arr[j+1] + 1
                j -= 1
            i = j
        print(arr)
        # for idx, n in enumerate(arr):
        #     if n == 0:
        #         arr[idx] = 1
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
