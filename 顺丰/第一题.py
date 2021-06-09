import math
if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for i, x in enumerate(arr):
        # n = n + x - math.ceil((n + x)/2)
        n = (n + x)//2
        # print(n)
    print(n)
