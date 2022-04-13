'''
0283 Move Zeros
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0 # The end of processed sequence
        right = 0 # The start of pre-processing sequence
        while right < len(nums):
            if nums[right] != 0:
                # Swap and move the tail cursor (left)
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1 #(move forward)