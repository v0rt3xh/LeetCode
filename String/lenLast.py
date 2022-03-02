'''
0058 Length of Last Word
'''
# Not fast enough, try harder
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        flag = False
        length = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ' and not flag:
                continue
            elif s[i] == ' ' and flag:
                break
            elif s[i] != ' ' and not flag:
                flag = True
                length += 1
            else:
                length += 1
        return length

#========
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        length = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ' and length == 0:
                continue
            elif s[i] == ' ' and length > 0:
                break
            elif s[i] != ' ':
                length += 1
        return length
        