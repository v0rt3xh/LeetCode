'''
0209 Minimum Size Subarray Sum
'''

'''
Brutal-Force,
Would exceed time limit =D
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        length = float('inf')
        for i in range(n):
            right = i + 1
            curSum = nums[i]
            while right < n and curSum < target:
                curSum += nums[right]
                right += 1
            if curSum >= target:
                length = min(length, right - i)
        return length if length != float('inf') else 0

'''
Sliding Window
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # special case
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1 # default answer
        start, end = 0, 0 # left right window boundary
        total = 0
        while end < n: # terminating condition
            total += nums[end] # expand right 
            while total >= s:
                # update answer
                ans = min(ans, end - start + 1)
                # compress left
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans
'''
Credit: leetcode-cn-solutions
'''

'''
Prefix Sum & Binary Search
Since all the numbers are positive, 
the prefix sum is in an ascending order.
'''
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1
        sums = [0] # Create a 'sorted' array
        for i in range(n):
            sums.append(sums[-1] + nums[i])
        # For every sum[:i]
        # find bound, such that 
        # bound >= i and sums[bound] - sums[i - 1] >= target
        for i in range(1, n + 1):
            target = s + sums[i - 1]
            bound = bisect.bisect_left(sums, target)
            if bound != len(sums):
                # bound - (i - 1) is the length
                ans = min(ans, bound - (i - 1))
        
        return 0 if ans == n + 1 else ans
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum/solution/chang-du-zui-xiao-de-zi-shu-zu-by-leetcode-solutio/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


