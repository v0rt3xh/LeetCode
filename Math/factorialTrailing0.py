'''
0172 Factorial Trailing Zeros
'''
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # What makes trailing zeros??
        '''
        5 as a divisor
        n // 5: How many number has one 5 as a divisor,
        n // 5 // 5: How many number has two 5s as divisors,
        ...
        Till 0. 
        Notice that each 5 contributes to a 10
        Thus count += n in the belowing script.

        One may argue, you said two 5's as divisor, why not *2?
        Cuz we have add the 5 in the first step (n // 5)
        say n = 131
        n // 5 = 26
        n // 5 // 5 = 5 (The five numbers are a subset of previous set!)
        n // 5 // 5 // 5= 1
        '''
        count = 0
        while n:
            n //= 5
            count += n
        return count