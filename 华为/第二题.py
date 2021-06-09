def preprocess(s):
    words = s.split()
    new_words = []
    punctuation = {'.', ',', '!', '?'}
    for word in words:
        if not word:
            continue
        pun = []
        while word[-1] in punctuation:
            if word[-1] == "?":
                pun.append(word[-1])
            else:
                pun.append('.')
            word = word[:-1]
        new_words.append(word.lower())
        new_words.extend(pun[::-1])
    return new_words

def dis(a, b):
    dp = [[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i in range(1, len(b)+1):
        dp[0][i] = i
    for i in range(1, len(a)+1):
        dp[i][0] = i
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                add, delete = dp[i][j-1] + 1, dp[i-1][j] + 1
                change = dp[i-1][j-1] + 2
                dp[i][j] = min(add, delete, change)
    return dp[len(a)][len(b)]




if __name__ == '__main__':
    s1, s2 = input().split(";")
    a = preprocess(s1)
    b = preprocess(s2)
    print(a)
    print(b)
    d = dis(a, b)
    print((d, len(b)))

