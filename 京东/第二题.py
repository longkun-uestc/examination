if __name__ == '__main__':
    m = int(input())
    array = []
    for i in range(m):
        op = input()
        if op[0] == '3':
            s = " ".join(map(str, array))
            print(s)
        elif op[0] == '1':
            _, x, y = list(map(int, op.split()))
            array.insert(x-1, y)
        else:
            _, x = list(map(int, op.split()))
            array.pop(x-1)

