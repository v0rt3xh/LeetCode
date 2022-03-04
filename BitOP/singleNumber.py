'''
0136 Single Number
well, this problem teach me the operation xor
a xor a = 0
a xor 0 = a 
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for num in nums:
            res ^= num
        return res
