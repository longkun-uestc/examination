def op1(arr):
    arr = arr[1:]+[arr[0]]
    return arr

def op2(arr):
    for i in range(0, len(arr), 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


if __name__ == '__main__':
    # n, m = list(map(int, input().split()))
    n = 5
    op = list(map(int, input().split()))
    i = 0
    length = len(op)
    while i < length:
        if op[i] == 2:
            j = i + 1
            count = 1
            while j < len(op) and op[j] == 2:
                j += 1
                count += 1
            if count % 2 == 0:
                op = op[:i] + op[j:]
            else:
                op = op[:i+1]+op[j:]
                i += 1
            length = len(op)
        else:
            j = i+1
            count = 1
            while j < len(op) and op[j] == 1:
                j += 1
                count += 1
            x = count // n
            op = op[:i] + op[i+n * x:]
            i = i + n * x + 1
            length = len(op)
    print(op)

