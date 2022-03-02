'''
0075 sort colors
'''



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Place 0 in the front, then place 1 in the front
        n = len(nums)
        if n == 1:
            return
        left = 0 
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1

# One-Pass
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        # Two pointers
        p0, p2 = 0, n - 1
        i = 0
        # If current element exceed the position of 2,
        # We've already finished the process.
        while i <= p2:
            # Be careful, nums[p0] could be 0 or 2
            # thus we need to keep swapping!
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            # for 0 , it's the same, because p0 start from the left
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1