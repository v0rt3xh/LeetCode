'''
0524 Longest Word in Dictionary through Deleting
Basic Approach:
Maintain two pointers
One on s, one on the words in dictionary.
'''

class Solution1:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        result = ""
        for word in dictionary:
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word):
                # Can be deleted & check length to update
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        return result

'''
Can sort first
Credit: Leetcode Solution @ Leetcode CN
'''
class Solution2:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        for t in dictionary:
            i = j = 0
            while i < len(t) and j < len(s):
                if t[i] == s[j]:
                    i += 1
                j += 1
            if i == len(t):
                return t
        return ""
