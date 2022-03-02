'''
0035 Search Insert Position
Typical binary search
if you think about the details, it's fun.
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                right = mid - 1
        return left

'''
Ending:
    smaller than target |  left (right + 1)
                 right  |  large than target
    left is the position!
'''