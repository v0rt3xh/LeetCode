'''
0031 Next Permutation

Some thoughts:
How can we get a larger number,
BUT... NOT THAT LARGE?

swap the large number (to the right) with the small number (to the left)
but also, should not be that large!
1. the large number should be close to the right end!
2. smaller large number swap
3. After swapping, the number following the large number should in ascending order

Find the first inverse from right to left 
1 - (i, j) next to each other but nums[i] < nums[j]
In this sense [j, end] must be descending!
2 - search in (i, end] from left to right get the last nums that is larger than nums[i]
3 - swap the two number, and rearrange the number after it in an ascending order!
if in 1 did not find anything, just invert the array!
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        # smart way to determine the "small number" 
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # "small number" exist or not
        if i >= 0:

            j = len(nums) - 1
            # swap the close right num and the small number
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # magic step, flip to ascending order
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

