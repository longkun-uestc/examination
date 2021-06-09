
def least(n, array):
    if n == 0:
        return []
    if len(array) == 1 and array[0] == "":
        return [-1]*n
    buffer = [-1] * n
    now = 0
    buffer_set = set()
    count_dict = {}
    index_dict = {}
    for num in array:
        if num in buffer_set:
            index = buffer.index(num)
            buffer.pop(index)
            buffer.insert(now-1, num)
        else:
            if now < len(buffer):
                buffer[now] = num
                now += 1
            else:
                buffer_set.remove(buffer[0])
                buffer.pop(0)
                buffer.append(num)
            buffer_set.add(num)
    return buffer


if __name__ == '__main__':
    import sys

    # x = int(sys.stdin.readline().strip())
    # array = sys.stdin.readline().strip().split(" ")
    # for i, a in enumerate(array):
    #     array[i] = int(a)
    import random
    # x = 5
    # array = [1, 2, 3, 4, 5, 2, 1, 6, 2]
    x = 100
    array = [random.randint(0, 10000) for i in range(1000000)]
    buffer = least(x, array)
    for i, a in enumerate(buffer):
        if i != len(buffer) - 1:
            print(a, end=" ")
        else:
            print(a)
    # setattr(self, 'fc%i' % i, fc)
