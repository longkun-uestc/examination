if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = list(map(int, input().split()))
        ops = []
        for j in range(m):
            op = input()
            ops.append(op)
        print("Case #%d:" % (i + 1))
        direction = 0
        move = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        x, y = 0, 0
        for op in ops:
            if op[0] == 'L':
                direction = (direction - 1 + 4) % 4
            elif op[0] == 'R':
                direction = (direction+1)%4
            elif op[0] == 'G':
                _, step = op.split()
                step = int(step)
                mv = move[direction]
                nx = x + mv[0] * step
                ny = y + mv[1] * step
                x = min(n-1, max(0, nx))
                y = min(n-1, max(0, ny))
            elif op[0] == 'P':
                print(str(y) + " " + str(x))



