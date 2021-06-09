def find(array, num):
    index = -1
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] < num:
            start = mid + 1
        elif array[mid] > num:
            end = mid - 1
        else:
            if mid + 1 < len(array) and array[mid] == array[mid + 1]:
                start = mid + 1
                index = mid + 1
            else:
                return mid
    return index


if __name__ == '__main__':
    import sys

    x = sys.stdin.readline().strip().split(",")
    num = int(sys.stdin.readline().strip())
    for i, a in enumerate(x):
        x[i] = int(a)
    b = find(x, num)
    print(b)
