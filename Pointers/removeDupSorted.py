'''
0080 Remove Duplicates from sorted array II
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        # Pre pointer for insert element
        # i pointer for moving around
        pre = 1
        curCount = 1
        curVal = nums[0]
        for i in range(1, n):
            if nums[i] == curVal:
                curCount += 1
                if curCount <= 2:
                    nums[pre] = curVal
                    pre += 1
            else:
                curCount = 1 
                curVal = nums[i]
                nums[pre] = curVal
                pre += 1
        return pre


# Fast slow ptr

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j
