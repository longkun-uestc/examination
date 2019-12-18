class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if len(numbers) < 2:
            return False
        numbers.sort()
        flag = False
        for i in range(0, len(numbers)):
            while numbers[i] != i:
                if numbers[i] != numbers[numbers[i]]:
                    tmp = numbers[numbers[i]]
                    numbers[numbers[i]] = numbers[i]
                    numbers[i] = tmp
                else:
                    duplication[0] = numbers[i]
                    flag = True
                    break
            if flag:
                break
        return flag

if __name__ == '__main__':
    s =Solution()
    x = [3,2,1,4,4]
    s.duplicate(x, [-1])

