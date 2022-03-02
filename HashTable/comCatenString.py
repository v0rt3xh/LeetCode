'''
0030 Substring with Concatenation of All Words
# Sliding window + hashset
'''
# Counter just help you resolve manual counting steps.

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter
        if not s or not words:return []
        # word length and word count
        one_word = len(words[0])
        all_len = len(words) * one_word
        n = len(s)
        # counter maintain
        # "abc": 1
        # those stuffs
        words = Counter(words)
        res = []
        # start from i, count the appearance of each seg word
        for i in range(0, n - all_len + 1):
            tmp = s[i:i+all_len]
            c_tmp = []
            for j in range(0, all_len, one_word):
                c_tmp.append(tmp[j:j+one_word])
            # compare it with the target counter
            if Counter(c_tmp) == words:
                res.append(i)
        return res

# Credit: leetcodeCN Powcai