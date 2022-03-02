'''
0026 Remove duplicates from sorted array
？？？ ...
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # imaginary ptr helps determine unique number!
        ptr = 1
        for i in range(1, n):
            # equals to previous one, just skip
            if nums[i] == nums[i - 1]:
                continue
            # meet unqiue stuff, put, increment ptr
            else:
                nums[ptr] = nums[i]
                ptr += 1
        return ptr