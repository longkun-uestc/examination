from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n_ids = -1
        for i, w in enumerate(words):
            if w == '':
                n_ids = i
                break
        res = []
        if n_ids != -1:
            for i, w in enumerate(words):
                if i != n_ids and self.is_huiwen(w):
                    res.append([n_ids, i])
        map_dict = {}
        for i, s in enumerate(words):
            map_dict[s[::-1]] = i
        for ids, word in enumerate(words):
            if ids == n_ids:
                continue
            for i in range(len(word)):
                if word[:i] in map_dict:
                    if self.is_huiwen(word[i:]) and ids != map_dict[word[:i]]:
                        res.append([ids, map_dict[word[:i]]])
                if word[i:] in map_dict:
                    if self.is_huiwen(word[:i]) and ids != map_dict[word[i:]]:
                        res.append([map_dict[word[i:]], ids])
        return res

    def is_huiwen(self, s):
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

if __name__ == '__main__':
    words = ["abcd","dcba","lls","s","sssll"]
    # words = ["bat","tab","cat"]
    # words = ['a', '']
    s = Solution()
    a = s.palindromePairs(words)
    print(a)
