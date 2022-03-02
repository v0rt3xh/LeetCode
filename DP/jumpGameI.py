'''
0055 Jump Game
'''
# Yep, the problem is simple, but the solution could get tricky.
# for i, its dp value should be the same for "all reachable indices"

'''
You just jump!
maxJump: reachable position
iterate throught the indices,
if at any time you find indices > maxJump 
you get rekt -> False
otherwise, to the end okay -> True
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        maxJump = 0
        for i in range(n):
            if i > maxJump:
                return False
            maxJump = max(maxJump, i + nums[i])
        return True