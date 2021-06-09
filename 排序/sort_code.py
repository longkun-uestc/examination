# 冒泡排序
def maopao(s):
    for i in range(len(s) - 1):
        for j in range(len(s) - i - 1):
            if s[j] > s[j + 1]:
                tmp = s[j]
                s[j] = s[j + 1]
                s[j + 1] = tmp


# 选择排序
def xuanze(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] > s[j]:
                tmp = s[i]
                s[i] = s[j]
                s[j] = tmp


# 插入排序
def charu(s):
    for i in range(1, len(s)):
        for j in range(i):
            if s[j] > s[i]:
                tmp = s[j]
                s[j] = s[i]
                s[i] = tmp


def charu1(s):
    for i in range(1, len(s)):
        get = s[i]
        j = i - 1
        while j >= 0 and s[j] > get:
            s[j + 1] = s[j]
            j -= 1
        s[j + 1] = get


# 归并排序
def guibin(s, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    guibin(s, start, mid)
    guibin(s, mid + 1, end)
    i = mid
    j = end
    tmp = [-1] * (end - start + 1)
    idx = len(tmp) - 1
    while i >= start and j > mid:
        if s[i] > s[j]:
            tmp[idx] = s[i]
            i -= 1
        elif s[i] <= s[j]:
            tmp[idx] = s[j]
            j -= 1
        idx -= 1
    while i >= start:
        tmp[idx] = s[i]
        i -= 1
        idx -= 1
    while j > mid:
        tmp[idx] = s[j]
        j -= 1
        idx -= 1
    s[start: end + 1] = tmp


# 快速排序
def kuaisu(s, start, end):
    if start < end:
        i, j = start, end
        now = s[start]
        while i < j:
            while i < j and s[j] >= now:
                j -= 1
            if i < j:
                s[i] = s[j]
                i += 1
            while i < j and s[i] < now:
                i += 1
            if i < j:
                s[j] = s[i]
                j -= 1
        s[i] = now
        print(start, now, s)
        kuaisu(s, start, i - 1)
        kuaisu(s, i + 1, end)

def maopao1(s):
    for i in range(len(s)):
        swap = False
        for j in range(len(s)-i-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                swap = True
        if not swap:
            break

def partion(s, i, j):
    now = s[i]
    while i < j:
        while i < j and s[j] >= now:
            j -= 1
        if i < j:
            s[i] = s[j]
            i += 1
        while i < j and s[i] < now:
            i += 1
        if i < j:
            s[j] = s[i]
            j -= 1
    s[i] = now
    return i

def quicksort(s, left, right):
    if left < right:
        pos = partion(s, left, right)
        quicksort(s, left, pos-1)
        quicksort(s, pos+1, right)

if __name__ == '__main__':
    s = [1, 2, 4, 7, 2, 3, 8, 4, 5]
    s = [5, 4, 7, 2, 1, 6, 3, 7, 8, 9]
    kuaisu(s, 0, len(s) - 1)
    # quicksort(s, 0, len(s)-1)
    print(s)
