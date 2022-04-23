'''
0287 Find the Duplicate Number
'''
# Naive approach
# Indeed, without modifying & constant extra space
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        cache = None
        for num in nums:
            if num == cache:
                return num
            cache = num
        return
'''
Can we improve it?
Fast - slow pointer
We have the array nums.
For position (index) i, we connect i with nums[i],
i = 0, 1, ..., n - 1
In other words, 
slow.next -> slow = nums[slow]
fast.next.next -> fast = nums[nums[fast]]
After they meet each other for the first time,
slow.next (from index 0)
fast.next 
Till next encouter -> res
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 # init 
        slow = nums[slow]
        fast = nums[nums[fast]] # Kinda like do while
                                # Since at the start, slow == fast
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
