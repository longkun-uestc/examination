def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    res = []
    while n > 1:
        if prime(n):
            res.append(n)
            break
        else:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    res.append(i)
                    n = n // i
                    break
    print(" ".join(map(str, res)))

