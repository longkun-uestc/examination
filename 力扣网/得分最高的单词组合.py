from typing import List


def check(word, letters):
    chars = set(list(word))
    for c in chars:
        w_count = word.count(c)
        l_count = letters.count(c)
        if w_count > l_count:
            return False
    return True


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if len(words) == 0:
            return 0
        w = words[0]
        if check(w, letters):
            w_score = 0
            residue_letters = letters[:]
            for c in w:
                score_ids = ord(c) - ord("a")
                w_score += score[score_ids]
                residue_letters.pop(residue_letters.index(c))
            return max(w_score + self.maxScoreWords(words[1:], residue_letters, score),
                       self.maxScoreWords(words[1:], letters, score))
        else:
            return self.maxScoreWords(words[1:], letters, score)



if __name__ == '__main__':
    # words = ["dog", "cat", "dad", "good"]
    # letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    # score = [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    words = ["leetcode"]
    letters = ["l", "e", "t", "c", "o", "d"]
    score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    s = Solution()
    a = s.maxScoreWords(words, letters, score)
    print(a)
