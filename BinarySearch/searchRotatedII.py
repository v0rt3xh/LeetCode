'''
0081 Search in Rotated Sorted Array II
repeated elements, sometimes you won't know
which half is sorted
'''
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                '''
                Not sure which part is sorted,
                have to shrink the range
                '''
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
                        
        
        