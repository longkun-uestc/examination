import collections
def least(n, array):
    if n == 0:
        return []
    if len(array) == 1 and array[0] == "":
        return [-1]*n
    buffer = [-1] * n
    now = 0
    buffer_set = set()
    count_dict = collections.OrderedDict()
    index_dict = {}
    for num in array:
        if num in buffer_set:
            count_dict[num] = 0
            for key in count_dict.keys():
                count_dict[key] += 1
        else:
            if now < len(buffer):
                index_dict[num] = now
                count_dict[num] = 0
                for key in count_dict.keys():
                    count_dict[key] += 1
                now += 1
            else:
                max_count = -1
                max_key = -1
                for key in count_dict.keys():
                    if count_dict[key] > max_count:
                        max_count = count_dict[key]
                        max_key = key
                index_dict[num] = index_dict[max_key]
                index_dict.pop(max_key)
                count_dict.pop(max_key)
                count_dict[num] = 0
                for key in count_dict.keys():
                    count_dict[key] += 1
            buffer_set.add(num)
    # count_dict = list(count_dict)
    # print(count_dict)
    count_dict = sorted(count_dict.items(), key=lambda a: a[1], reverse=True)
    now = 0
    for key in count_dict:
        buffer[now] = key[0]
        now += 1
    return buffer


if __name__ == '__main__':
    import sys

    # x = int(sys.stdin.readline().strip())
    # array = sys.stdin.readline().strip().split(" ")
    # for i, a in enumerate(array):
    #     array[i] = int(a)
    import random
    x = 5
    array = [1, 2, 3, 4, 5, 2, 1, 6, 2]
    x = 100
    array = [random.randint(0, 10000) for i in range(1000000)]
    buffer = least(x, array)
    for i, a in enumerate(buffer):
        if i != len(buffer) - 1:
            print(a, end=" ")
        else:
            print(a)
