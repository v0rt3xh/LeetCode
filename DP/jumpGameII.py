'''
0045 Jump Game II
An observation:
    The minimum jump needed to an element,
    must also be the minimum jump to the travelled elements.
    Assume that the first index > 0 
    Greedy approach must work! O(n^2) must exceed time lmao
    How to 'apply' a DP approach??
    Greedy forward search
        start from i, we record the maximum index it can reach,
        by saying maximum, I mean at the !next point! we can reach even further
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        resStep, maxPos, end = 0, 0, 0
        '''
        resStep: step it takes to reach the end
        maxPos: current maximum leap position
        end: last achievable right boundary
        '''
        for i in range(n - 1):
            if maxPos >= i:
                # update the posible region
                maxPos = max(maxPos, i + nums[i])
                if i == end: # reach current right boundary
                    end = maxPos # should update to the maximum position
                    resStep += 1 # jump
        return resStep
        
        