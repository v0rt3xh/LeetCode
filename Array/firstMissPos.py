'''
0041 First Missing Positive
O(n) time & O(1) space
Tricky boi!
return the smallest missing positive integer
'''

'''
First, try to come up with some intuitive ideas
Use a super large hash table,
place every positive number in it,
then iterate from 1 to _ 
O(N) + O(N)
'''

# How can we make the space O(1)
# i.e., we choose to modify the given array.
# How to define a hash table on our own??

'''
For an array with length N
The missing positive number must reside in [1, N + 1]!!!
If we put the numbers within [1, N] into the "hash table",
we can find the target.
'''

'''
Then, the problem becomes how to create the key-value pair.
First, iterate through the whole array, replace non-positive values by N + 1
Second, iterate through the whole array, 
if the number is within [1, N], say n modify nums[n - 1] 
adding a negative symbol to nums[num - 1],
thus, we need to use abs
At last, iterate the whole array, get the first index that are not negative and with in 1 N+1
RETURN THAT INDEX + 1
DAMN THAT WAS NUTS!!!!!!
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        # Flip negative terms to N + 1
        for i in range(N):
            if nums[i] <= 0:
                nums[i] = N + 1
        for i in range(N):
            # abs needed to creating the key-value pair
            num = abs(nums[i])
            # The num is with in N
            if num <= N:
                # Add the tricky negative symboool
                # abs though
                nums[num - 1] = -abs(nums[num - 1])
        # retrieve the index and we are done.
        for i in range(N):
            if nums[i] > 0:
                return i + 1
        # No index? Then N + 1 ROFL
        return N + 1