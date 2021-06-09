if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        arr = []
        while True:
            s = input()
            if not s:
                break
            arr.append(s)
        words = []
        for s in arr:
            w = s.split()
            w = [c for c in w if c]
            words.append(w)
        idx = 0
        length = len(words)
        while idx < length:
            now_vector = words[idx]
            count = len(now_vector) - 1
            nums = [len(w) for w in now_vector]
            count += sum(nums)
            last = idx - 1
            last_value = -1
            if last >= 0:
                last_vector = words[last]
                if len(last_vector[-1]) + 1 <= n - count:
                    last_value = len(last_vector[-1]) + 1
            next = idx + 1
            next_value = -1
            if next < length:
                next_vector = words[next]
                if len(next_vector[0]) + 1 <= n - count:
                    next_value = len(next_vector[0]) + 1
            if last_value == -1 and next_value == -1:
                idx += 1
            else:
                if last_value > next_value:
                    word = words[idx - 1].pop()
                    words[idx].insert(0, word)
                else:
                    word = words[idx + 1].pop(0)
                    words[idx].insert(-1, word)
                idx += 1
        print(words)
        for now_vector in words:
            c = len(now_vector) - 1
            nums = [len(w) for w in now_vector]
            count = sum(nums) + c
            space = n - count
            p = space // c
            q = space % c
            print(p, q, count)
            for i in range(c):
                now_vector[i] = now_vector[i] + p * " "
            for i in range(c, c-q, -1):
                now_vector[i] = " " + now_vector[i]
            s = " ".join(now_vector)
            print(s, len(s))
        print('')



