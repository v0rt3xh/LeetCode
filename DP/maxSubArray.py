'''
0053 Maximum Subarray
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp
        # dp[i]: the maximum sum possible ending with nums[i]
        n = len(nums)
        pre = nums[0]
        res = pre
        for i in range(1, n):
            pre = max(pre + nums[i], nums[i])
            res = max(pre, res)
        return res
            