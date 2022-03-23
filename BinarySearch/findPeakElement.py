'''
0162 Find Peak Element
Have I seen you in the algorithm class?
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums = [float('-inf')] + nums + [float('-inf')]
        left = 1
        right = len(nums) - 2
        while left < right:
            mid = (left + right) // 2
            # Binary search part
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid - 1 # find then return
            # mid cannot be the element!
            # mid - 1 possible
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            # mid + 1 possible
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
        return left - 1