def check_iou(a, b):
    inter = max(a + b) - min(a + b)
    if inter < (a[1] - a[0]) + (b[1] - b[0]):
        return True
    else:
        return False


def get_iou(a, b):
    arr = a + b
    arr.sort()
    return [arr[1], arr[2]]
N = int(input())

array = []
for i in range(N):
    arr = list(map(int, input().split()))
    array.append(arr)
max_c = -1
for i in range(len(array)):
    count = 1
    start = array[i]
    for j in range(i+1, len(array)):
        if check_iou(start, array[j]):
            count += 1
            start = get_iou(start, array[j])
    max_c = max(max_c, count)
print(max_c)



