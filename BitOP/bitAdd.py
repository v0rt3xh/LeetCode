'''
0067 bit Addition
My approach: Simulation
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        diff = abs(len(a) - len(b))
        # inflate with zeros
        if len(a) < len(b):
            for _ in range(diff):
                a = '0' + a
        if len(b) < len(a):
            tool = []
            for _ in range(diff):
                b = '0' + b
        # carry over
        carry = 0
        res = ''
        n = len(a)
        for i in range(n):
            curSum = int(a[n - 1 - i]) + int(b[n - 1 - i]) + carry
            carry = curSum // 2
            curDigit = curSum % 2
            res = str(curDigit) + res
        if carry:
            res = str(carry) + res
        return res

# Digit operation

        

