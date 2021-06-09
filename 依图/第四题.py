def search(array, x):
    l, r = 0, len(array) - 1
    while l < r:
        mid = (l+r) // 2
        if array[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return l


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    count = 0
    for i in range(len(arr)):
        now = arr[i]
        j = len(arr) - 1
        tmp = []
        while j > i:
            while j > i and arr[j]<=arr[i]:
                j -= 1
            idx = search(tmp, arr[j])
            count += idx
            tmp = tmp[:idx] + [arr[j]] + tmp[idx:]
            tmp.insert(idx, arr[j])




