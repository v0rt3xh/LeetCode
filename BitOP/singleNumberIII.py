'''
0260 Single Number III
Divide those numbers into 2 groups.
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xorSum = 0
        for num in nums:
            xorSum ^= num
            
        lowestOne = xorSum & (-xorSum)
        first, second = 0, 0
        for num in nums:
            if num & lowestOne:
                first ^= num
            else:
                second ^= num
        return [first, second]