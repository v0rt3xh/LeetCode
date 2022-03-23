'''
0171 Excel Sheet Column Number
'''
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        i = 0
        res = 0
        while i < n:
            # In 0168, we use num - 1
            # Here, we add 1 to the difference
            diff = ord(columnTitle[i]) - ord('A') + 1
            res = diff + 26 * res # 26 as the multiplier
            i += 1
        return res