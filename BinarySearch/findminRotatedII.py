'''
0154 Find Minimum in Rotated Sorted Array II
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # Must in the left half
                right = mid
            elif nums[mid] > nums[right]:
                # must in the right half, and not inclued mid.
                left = mid + 1
            else:
                # avoid duplicates, shrink the interval
                right -= 1
        return nums[left]
