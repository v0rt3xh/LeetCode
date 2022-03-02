'''
0028 strStr
KMP algorithm
I was like ???
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        n = len(haystack)
        targetLen = len(needle)
        for i in range(n - targetLen + 1):
            if haystack[i: (i + targetLen)] == needle:
                return i
        return -1