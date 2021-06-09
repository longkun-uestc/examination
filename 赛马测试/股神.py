while 1:
    n = int(input())
    i = 1
    while i*(i+1)/2 <= n:
        i += 1

    s = 1
    for j in range(1, i-1):
        s += j-1
    sub_n = n - (i-1)*(i)/2
    s += sub_n
    print(s)
