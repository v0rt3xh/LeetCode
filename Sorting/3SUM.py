'''
0015 3SUM
3-tuple (num_i, num_j, num_k) 
such that num_i + num_j + num_k = 0
while i != j != k
Also, your solution should not include duplicated elements.

SORT + DOUBLE POINTER
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        n = len(nums)
        # To help us avoid duplicated tuples, 
        # we sort the array first.
        res = []
        nums.sort()
        # Outer loop: the first number
        for first in range(n):
            # Just to help us avoid duplicate enumeration
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            third = n - 1
            # introduce double pointer, why?
            # cuz need nums[second] + nums[third] == nums[first]
            # as second increase, third should decrease!
            for second in range(first + 1, n):
                # Also, avoid duplicate seconds!
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # Now begin the double pointer magic
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                    # Get smaller 'third'
                # if we observe that second is equal to third
                # hands down, would only increase, not possible
                # just break
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    res.append([nums[first], nums[second], nums[third]])
        return res
                
                