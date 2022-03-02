'''
0006 ZigZag Conversion

'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only require one row
        # just return the input
        if numRows == 1:
            return s
        # First edition, i use a naive approach
        # 2D array not needed!
        # Bruh no need array!!!
        # just '' should suffice
        res = [[''] for _ in range(numRows)]
        start = 1
        increment = 1
        for c in s:
            # Back to start
            # need to increment
            if start == 1:
                increment = 1
            # Reach the bottom
            # need to decrease
            if start == numRows:
                increment = -1
            # put the num into the array
            res[start - 1].append(c)
            start += increment
        resStr = ''
        # Thus, not the smartest method 
        for strList in res:
            for c in strList:
                resStr += c
        return resStr
        