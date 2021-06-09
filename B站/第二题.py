def get_count(n):
    flag = get_prime(n)
    count = 0
    for i in range(len(flag)):
        if flag[i]:
            s = i
            if s == n:
                count += 1
                continue
            for j in range(i+1, len(flag)):
                if flag[j]:
                    s += j
                    if s == n:
                        count += 1
                        break
                    elif s > n:
                        break
    return count


def get_prime(n):
    flag = [True for i in range(n+1)]
    flag[0] = False
    flag[1] = False
    for i in range(2, n+1//2):
        count = 2
        while i*count < n+1:
            flag[i*count] = False
            count += 1
    return flag

if __name__ == '__main__':
    n = int(input())
    c = get_count(n)
    print(c)

