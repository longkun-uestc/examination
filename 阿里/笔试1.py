def out_put(n, array):
    for i in range(1, n + 1):
        if i not in array:
            if array and array[-1] != i + 1 and array[-1] != i - 1:
                array.append(i)
                out_put(n, array)
x = []
def out_put1(n, arrs):
    new_arrs = []
    flag = True
    for a in arrs:
        if len(a) == n:
            x.append(a)
            continue
        for i in range(1, n+1):
            if i not in a and a[-1] != i+1 and a[-1]!=i-1:
                s = a + [i]
                new_arrs.append(s)
    if len(new_arrs) == 0:
        return
    out_put1(n, new_arrs)



def all_array(n):
    if n <= 3:
        return
    for i in range(1, n + 1):
        array = [i]
        out_put(n, array)
        if len(array) == n:
            s = ' '.join(list(map(str, array)))
            print(s)

if __name__ == '__main__':
    n = int(input())
    # all_array(n)
    arrays = [[i] for i in range(1, n+1)]
    out_put1(n, arrays)
    print(x)
    # for a in arrays:
    #     print(a)
