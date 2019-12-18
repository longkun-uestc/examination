# 这种方法比较垃圾
def find_min(numbers):
    if len(numbers) == 1:
        return 0
    # print("number", numbers)
    b = sorted(numbers)
    print(b)
    if len(set(numbers)) == 1:
        return 0
    if b[0][0] == b[1][0]:
        next = []
        for i in range(len(numbers)):
            if len(numbers[i]) > 1:
                next.append(numbers[i][1:])
            else:
                next.append(numbers[i])
        result = find_min(next)
        return result
    else:
        for i in range(len(numbers)):
            if numbers[i] == b[0]:
                return i


def find_same(numbers):
    tmp = sorted(numbers)
    result = [tmp[0]]
    for i in range(1, len(tmp)):
        if tmp[i][0] == tmp[0][0]:
            result.append(tmp[i])
        else:
            break
    return result


class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ""
        numbers = [str(num) for num in numbers]
        s = ""
        while numbers:
            same = find_same(numbers)
            numbers = set(numbers).difference(set(same))
            while same:
                ids = find_min(same)
                s += same[ids]
                same.pop(ids)
        return int(s)


# 冒泡排序的方法，更简单
def cmp(a,b):
    if a[0] > b[0]:
        return True
    if a[0] < b[0]:
        return False
    if a[0] == b[0] and len(a)==1 and len(b) == 1:
        return False
    else:
        if len(a) > 1:
            a = a[1:]
        if len(b) > 1:
            b = b[1:]
        print(a, b)
        return cmp(a,  b)
class newSolution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ""
        numbers = [str(num) for num in numbers]
        for i in range(0, len(numbers)):
            for j in range(i, len(numbers)):
                if cmp(numbers[i], numbers[j]):
                    tmp = numbers[i]
                    numbers[i] = numbers[j]
                    numbers[j] = tmp
        s = ""
        for n in numbers:
            s += n
        return int(s)


if __name__ == '__main__':
    # x = '3'
    # y = '321'
    # a = cmp(x, y)
    # print(a)
    # print(x, y)
    # exit()

    x = [3, 321, 4, 326, 43, 15]
    # x = [1,1,11]
    new_method(x)
    exit()
    s = Solution()
    a = ["3", '32', '321', '4']
    b = ['4']
    # print(set(a).difference(b))
    # exit()
    a = s.PrintMinNumber(x)
    print(a)
