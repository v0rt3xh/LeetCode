'''
0014 Longest Common Prefix
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cursor = 0
        if not strs[0]:
            return ""
        flag = True
        while True:
            if cursor >= len(strs[0]):
                break
            prefix = strs[0][cursor]
            for c in strs:
                if cursor >= len(c) or c[cursor] != prefix:
                    flag = False
                    break
                else:
                    continue
            if not flag:
                break
            cursor += 1
        return strs[0][: cursor]