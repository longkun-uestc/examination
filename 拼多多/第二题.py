def get_tuple(arr):
    top_down = arr[:2]
    left_right = arr[2:4]
    front_back = arr[4:]
    top_down.sort()
    left_right.sort()
    front_back.sort()
    res = [top_down, left_right, front_back]
    res.sort(key=lambda x:x[0])
    res = [tuple(x) for x in res]
    return tuple(res)


if __name__ == '__main__':
    N = int(input())
    array = []
    for i in range(N):
        arr = list(map(int, input().split()))
        array.append(arr)

    count_dict = {}
    for arr in array:
        key = get_tuple(arr)
        print(key)
        if key not in count_dict:
            count_dict[key] = 1
        else:
            count_dict[key] += 1

    print(len(count_dict))
    count = []
    for key, c in count_dict.items():
        count.append(c)
    count.sort(reverse=True)
    s = ' '.join(list(map(str, count)))
    print(s)


