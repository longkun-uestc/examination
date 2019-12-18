class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) <= 1 or len(numbers) > 13:
            return False
        # map_dict = {'J': 11, "Q": 12, "K": 13, "A": 1, "0": 0}
        # numbers = [int(n) if "2" <= n <= "10" else map_dict[n] for n in numbers]
        numbers.sort()
        count_0 = numbers.count(0)
        numbers = numbers[count_0:]
        start = 0
        while start < len(numbers) - 1:
            if count_0 == 0:
                break
            if numbers[start + 1] - numbers[start] >= 2:
                numbers.insert(start + 1, numbers[start] + 1)
                count_0 -= 1
                start += 1
            else:
                start += 1
        result = True
        for i in range(0, len(numbers) - 1):
            if (numbers[i + 1] - numbers[i]) != 1:
                result = False
                break
        # print(numbers)
        # print(result)
        return result


        # if len(numbers) <= 1:
        #     return True
        # if len(list(set(numbers))) < len(numbers):
        #     return False
        # for i in range(1, len(numbers)):
        #     if numbers[i] -numbers[i-1]>


if __name__ == '__main__':
    s = Solution()
    x = [1, 2, 5, 6, 7, 0, 0, 0, 11]
    x = [0, 0]
    s.IsContinuous(x)
