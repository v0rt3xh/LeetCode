'''
0016 3SUM closest
a little bit different.
We sort first
Then start from the first component.
Place two pointers on the two ends of remaining parts.
second = first + 1
third = n - 1
Then when current sum > target, move the third: third -= 1
     when current sum < target, move the second: second += 1
check and update
O(N^2) ACHIEVED.
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        n = len(nums)
        for first in range(n):
            # Remove duplications
            # bonus: can do the same thing to second and third!
            if first != 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            second = first + 1
            while second < third:
                cur = nums[second] + nums[third] + nums[first]
                if cur > target:
                    third -= 1
                else:
                    second += 1
                # A comparison
                if abs(cur - target) < abs(res - target):
                    res = cur
                if cur == target:
                    return target
        return res
                    
                    
                
        
        