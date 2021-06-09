def number(n, k, K):
    if n == 0 and k == 0:
        return 1
    if n == 0 and k != 0:
        return 0
    if n > 0:
        if k == 0:
            return number(n - 1, 1, K) * 2
        else:
            return number(n - 1, k - 1, K) + number(n - 1, (k + 1) % K, K)


def number1(N, k):
    ai_1 = 1
    ai = 0
    ai_2 = -1
    for i in range(1, N + 1):
        ai_2 = (k - 1) * ai_1 + (k - 2) * ai
        ai_1 = ai
        ai = ai_2
    return ai_1 % 1000000007


if __name__ == '__main__':
    N, K = list(map(int, input().split(' ')))
    count = number1(N, K)
    print(count)
