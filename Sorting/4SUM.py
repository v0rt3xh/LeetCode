'''
0018 4SUM
Remove duplications!!!!!
Those pointers!!!
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # Special case: do nothing!
        if n < 4:
            return []
        # sort for operations
        nums.sort()
        resList = []
        # left most component's possible position up to n - 4
        for i in range(n - 3):
            # remove duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # second left most item's indices
            for j in range(i + 1, n - 2):
                # remove duplicates
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                # double pointers come in
                left = j + 1
                right = n - 1
                while left < right: 
                    curSum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curSum == target:
                        resList.append([nums[i], nums[j], nums[left], nums[right]])
                        # remove duplicates!
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # point to the different location, thus + 1
                        left += 1
                        # similar for the right one 
                        while left < right and nums[right] ==nums[right - 1]:
                            right -= 1
                        right -= 1
                    # also the double pointers movement
                    elif curSum < target:
                        left += 1
                    
                    else:
                        right -= 1
        return resList