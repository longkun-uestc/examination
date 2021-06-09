if __name__ == '__main__':
    m = int(input())
    array = []
    ops = []
    for i in range(m):
        op = input()
        ops.append(op)
    i = 0
    while i < len(ops):
        now = ops[i]
        op = now[0]
        if op == '3':
            s = " ".join(array)
            print(s)
            i += 1
        elif op == '1':
            j = i + 1
            kv = []
            while j < len(ops) and ops[j][0] == op:
                _, x, y = ops[j].split()
                kv.append([x-1, y])
                j += 1
            kv.sort(key=lambda v:v[0])
            


