if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        W = list(map(int, input().split()))
        q = int(input())
        for __ in range(q):
            x, y, z = list(map(int, input().split()))
            total = x*y*z
            idx = -1
            price = -1
            diff = float('inf')
            for i, w in enumerate(W):
                c = total - w
                if c < 0:
                    continue
                else:
                    if c < diff:
                        diff = c
                        price = w
                        idx = i
            if idx != -1:
                print(idx+1, price)
            else:
                print(-1)