'''
0164 Maximum Gap
O(N) Run time
O(N) Extra Space
All nonnegative numbers
'''
# 1. Naive approach, just sort, and check successive elements.
# O(NlogN) + O(1) space
# How can we do it in linear time?
# 2. Radix Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0 
        RADIX = 10
        placement = 1
        max_digit = max(nums)
        while placement <= max_digit:
            buckets = [list() for _ in range(RADIX)]
            for i in nums:
                tmp = int((i / placement) % RADIX)
                buckets[tmp].append(i)
            a = 0
            for b in range(RADIX):
                for i in buckets[b]:
                    nums[a] = i
                    a += 1
            placement *= RADIX
        
        res = 0
        for i in range(n - 1):
            if nums[i + 1] -nums[i] > res:
                res = nums[i + 1] -nums[i]
        return res
'''
Credit: https://github.com/TheAlgorithms/Python/blob/master/sorts/radix_sort.py
& @Fzldq 
'''


