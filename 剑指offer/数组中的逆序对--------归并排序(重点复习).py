def inversePairsCore(data, copy, start, end):
    if start == end:
        copy[start] = data[start]
        return 0
    mid = (start + end) // 2
    left = inversePairsCore(copy, data, start, mid)
    right = inversePairsCore(copy, data, mid + 1, end)
    i, j, copy_index = (mid, end, end)
    count = 0
    while i >= start and j >= mid + 1:
        if data[i] > data[j]:
            copy[copy_index] = data[i]
            count += j - mid  # count = count + (j-(mid+1))+1
            i -= 1
            copy_index -= 1
        else:
            copy[copy_index] = data[j]
            j -= 1
            copy_index -= 1
    while i >= start:
        copy[copy_index] = data[i]
        i -= 1
        copy_index -= 1
    while j >= mid + 1:
        copy[copy_index] = data[j]
        j -= 1
        copy_index -= 1
    return count + left + right


def mergeSort(data, begin, end):
    if begin == end - 1:
        return 0
    mid = int((begin + end) / 2)
    left_count = mergeSort(data, begin, mid)
    right_count = mergeSort(data, mid, end)
    merge_count = merge(data, begin, mid, end)
    return left_count + right_count + merge_count


def merge(data, begin, mid, end):
    i = begin
    j = mid
    count = 0
    temp = []
    while i < mid and j < end:
        if data[i] <= data[j]:
            temp.append(data[i])
            i += 1
        else:
            temp.append(data[j])
            j += 1
            count += mid - i
    while i < mid:
        temp.append(data[i])
        i += 1
    while j < end:
        temp.append(data[j])
        j += 1
    data[begin: end] = temp
    del temp
    return count


class Solution:
    def InversePairs(self, data):
        if len(data) == 0:
            return 0
        # begin = 0
        # end = len(data)
        # ans = mergeSort(data, begin, end)
        # print(ans)
        # return ans % 1000000007
        copy = data[:]
        count = inversePairsCore(data, copy, 0, len(data) - 1)
        return count % 1000000007


# 归并排序
def sort_by_merge(data, start, end):
    if start == end:
        return 0
    # if end - start == 1:
    #     if data[start] > data[end]:
    #         tmp = data[start]
    #         data[start] = data[end]
    #         data[end] = tmp
    #     return 0
    mid = (start + end) // 2
    sort_by_merge(data, start, mid)
    sort_by_merge(data, mid + 1, end)
    i = mid
    j = end
    copy = [-1] * (end - start + 1)
    copy_index = len(copy) - 1
    while i >= start and j >= mid + 1:
        if data[i] > data[j]:
            copy[copy_index] = data[i]
            copy_index -= 1
            i -= 1
        else:
            copy[copy_index] = data[j]
            copy_index -= 1
            j -= 1
    while i >= start:
        copy[copy_index] = data[i]
        copy_index -= 1
        i -= 1
    while j >= mid + 1:
        copy[copy_index] = data[j]
        j -= 1
        copy_index -= 1
    data[start: end + 1] = copy


if __name__ == '__main__':
    x = [1, 5, 4, 2, 3, 8, 11, 6, 2, 4, 3, 100, 16]
    sort_by_merge(x, 0, len(x) - 1)
    print(x)
    x = [1, 2, 3, 4, 5, 6, 7, 0]
    s = Solution()
    s.InversePairs(x)
