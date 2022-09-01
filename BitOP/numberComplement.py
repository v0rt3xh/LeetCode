'''
0476 Number Complement
Deal with leading zeros.
Then take ~num.
'''
class Solution:
    def findComplement(self, num: int) -> int:
        base = 1
        res = 0
        while num:
            value = 0 if num % 2 else 1
            res += base * value
            base *= 2
            num = num >> 1
        return res
        