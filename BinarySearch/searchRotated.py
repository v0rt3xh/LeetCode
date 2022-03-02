'''
0033 Search in Rotated Sorted Array
Binary search variation
There is an integer array nums, sorted in ascending order.
Rotated at a pivot index k 
[nums[k], nums[k + 1], ..., nums[n - 1], nums[0], nums[1],.....]
You need to have the right logic.
One important finding:
One half must have be ordered!
still 
1. mid == target
    ez
Then, we need to determine which part is sorted.
nums[mid] <= nums[-1] (mid + 1, right) is sorted
    nums[mid] <= target < nums[right]
        left = mid + 1
    else
        right = mid - 1
nums[mid] >= nums[0] (left, mid - 1) is sorted
    nums[left] <= target < nums[mid]
        right = mid - 1
    else
        left = mid + 1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # We consider which part is sorted!
            # Case 1: The left half is sorted
            if nums[left] <= nums[mid]:
                # 1.1 target is within the range
                #     shrink right
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # 1.2 Not!
                #     right half possible, move left
                else:
                    left = mid + 1
            # Case 2: The right half is sorted ....
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1