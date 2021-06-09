from typing import List
import re
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        if not s and words == ['']:
            return [0]
        count_dict = {}
        for w in words:
            if w not in count_dict:
                count_dict[w] = 1
            else:
                count_dict[w] += 1
        one_l = len(words[0])
        word_l = one_l * len(words)
        res = []
        for i in range(len(s)-word_l+1):
            sub_s = s[i:i+word_l]
            s_dict = {}
            for j in range(0, word_l, one_l):
                if sub_s[j:j+one_l] not in s_dict:
                    s_dict[sub_s[j:j+one_l]] = 1
                else:
                    s_dict[sub_s[j:j + one_l]] += 1
            if s_dict == count_dict:
                res.append(i)
        print(res)
        return res



if __name__ == '__main__':
    s = Solution()
    y = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    y = "barfoothefoobarman"
    words = ["foo", "bar"]
    y = 'aaa'
    words=['a', 'a']
    # is_used = [False, False, False, False]
    # s.get_order("", words, is_used)
    # print(s.str_dict)
    s.findSubstring(y, words)



