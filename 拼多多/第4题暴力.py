if __name__ == '__main__':
    N,M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    count = 0
    visit = set()
    for i in range(1, N+1):
        for j in arr:
            if i % j == 0:
                visit.add(i)
                break
    print(visit)
    print(len(visit))