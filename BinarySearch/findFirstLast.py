'''
0034 Find First and Last Position of Element in Sorted Array
Required O(logN) time
One caution: 
    the template or technical details of Binary Search
    SHOULD BE THE SAME!!!!
    Just modify your target...
'''

#### Define a function that conduct binary search to find bounds

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # looks so familiar 
        # find_bound find the first element that is not smaller than target!
        def find_bound(nums, target):
            n = len(nums)
            left = 0
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
        # the tricky boy use target + 1 -> locate the last position...
        a, b = find_bound(nums, target), find_bound(nums, target + 1)
        # a == len(nums), just out of bound
        # not equal -> wasted
        # b - 1 then should be great
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        else:
            return [a, b - 1]
