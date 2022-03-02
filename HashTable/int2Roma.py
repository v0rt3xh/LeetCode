'''
0012 integer to Roman

First step, create a symbol hashset
Start from the input num
Find the closest symbol in the hashset
i.e. num >= that symbol's value
while num >= that symbol.val:
    minus the value and append symbol!
if num after the process is 0: stop!
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        codeMap = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        res = ''
        while num:
            for value, symbol in codeMap:
                while value <= num:
                    num -= value
                    res += symbol
                if num == 0:
                    break
        return res
        