def get_max(s): # s为空？
    if not s:
        return 0
    if len(set(s)) == len(s):
        return 2
    color = s[0]
    i = 1
    while i < len(s) and s[i] == color:
        i += 1
    if i == len(s):
        return i
    last = [0, i-1, i, color]
    max_seq = [0, i-1, i, color]
    flag = False
    while i < len(s):
        if i + 1 < len(s) and s[i+1] == last[-1]:
            j = i + 1
            while j < len(s) and s[j] == last[-1]:
                j += 1
            now = [i+1, j-1, j-i-1, last[-1]]
            new = [last[0], j-1, j-last[0], last[-1]]
            max_seq = new if new[2] > max_seq[2] else max_seq
            if not flag or max_seq == new:
                flag = True
            last = now
            i = j
        else:
            j = i + 1
            while j<len(s) and s[j] == s[i]:
                j += 1
            now = [i, j-1, j-i, s[i]]
            max_seq = now if now[2] > max_seq[2] else max_seq
            last = now
            i = j
    if flag:
        return max_seq[2]
    else:
        return max_seq[2] + 1

def get_max1(s, k=1):
    from collections import defaultdict
    maxLen, windowStart, maxFreq = 0, 0, 0
    # 统计出现频率
    freqDict = defaultdict(int)
    for windowEnd in range(len(s)):
        rightChar = s[windowEnd]
        freqDict[rightChar] += 1
        # 保存历史出现的最大频率
        maxFreq = max(freqDict[rightChar], maxFreq)
        # 缩小滑动窗口
        if (windowEnd - windowStart + 1 - maxFreq) > k:
            leftChar = s[windowStart]
            windowStart += 1
            freqDict[leftChar] -= 1
        maxLen = max(maxLen, windowEnd - windowStart + 1)
    return maxLen





if __name__ == '__main__':
    M = int(input())
    arr = []
    for i in range(M):
        s = input()
        arr.append(s)
    for a in arr:
        l = get_max1(a)
        print(l)

