'''
0027 Remove Element
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == val:
                continue
            else:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr