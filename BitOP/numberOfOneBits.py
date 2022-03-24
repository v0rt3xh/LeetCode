'''
0191 Number of 1 Bits
'''
'''
First, a very naive approach.
Just count!
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Constant traversal time?
        # Count 1, n >> 1?
        # Not fast enough
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

'''
Smarter, start from the leftmost 1
How to retrieve that?
A bit tricky bit operation 
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        # n & (n - 1), clear the right most 1
        # clear until no zeros in it
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count