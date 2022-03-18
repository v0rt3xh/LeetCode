'''
0168 Excel Sheet Column Title
I find it tricky...
Use columnNumber - 1 instead
Bro, that was impressive.
'''
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabets = string.ascii_uppercase
        res = ''
        while columnNumber:
            remain = (columnNumber - 1) % 26
            columnNumber = (columnNumber - 1) // 26
            res = alphabets[remain] + res
        return res
'''
Reasons behind the -1:
    Suppose now
        A   1
        B   2
        C   3
        D   4
        ..
        J   10
    Our starting point is not zero. 
    Should convert to natural numbers!
'''