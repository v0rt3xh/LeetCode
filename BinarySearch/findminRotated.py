'''
0153 Find Minimum in Rotated Sorted Array
'''
'''
My initial solution, complicated ...
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # if mid smaller than right
            # right half is sorted
            if nums[mid] <= nums[right]:
                # but we need to make sure min not in the left half
                if nums[mid - 1] <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # otherwise, left part is sorted
            # the min must be on the right side
            else: 
                left = mid + 1
        return nums[right]

'''
Official Sol
The last element in the array matters, suppose it's x
All elements to the left of the min, should be larger than x
All elements to the right of the min, should be smaller than x
    low: left bound
    high: right bound 
    pivot: mid
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        # when length is one, end the iteration
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                # the elements in the right half: larger than min
                high = pivot 
            else: # the elements in the left half: larger than min
                low = pivot + 1
        return nums[low]
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-xu-shu-zu-zhong-5irwp/
来源：力扣（LeetCode）
'''