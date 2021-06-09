N = int(input())


def check_iou(a, b):
    inter = max(a + b) - min(a + b)
    if inter < (a[1] - a[0]) + (b[1] - b[0]):
        return True
    else:
        return False


def get_iou(a, b):
    arr = a + b
    arr.sort()
    return arr[1], arr[2]


array = []
for i in range(N):
    a = list(map(int, input().split()))
    array.append(a)

iou = set()
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if check_iou(array[i], array[j]):
            s, e = get_iou(array[i], array[j])
            if (s, e) not in iou:
                iou.add((s, e))
length = -1
while len(iou) != length:
    length = len(iou)
    i = 0
    j = i+1
    new_iou = set()
    iou_list = list(iou)
    for i in range(len(iou_list)):
        a = list(iou_list[i])
        for j in range(i+1, len(iou_list)):
            b = list(iou_list[j])
            if check_iou(a, b):
                s, e = get_iou(a, b)
                if (s, e) not in new_iou:
                    new_iou.add((s, e))
    if not new_iou:
        break
    iou = new_iou
max_l = -1
for x in iou:
    c = 0
    for arr in array:
        if check_iou(list(x), arr):
            c += 1
    max_l = max(max_l, c)
print(max_l)



