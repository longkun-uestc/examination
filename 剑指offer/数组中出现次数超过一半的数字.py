class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if len(numbers) == 0:
            return 0
        all = list(set(numbers))
        for num in all:
            count = numbers.count(num)
            if count > len(numbers)/2:
                return num
        return 0