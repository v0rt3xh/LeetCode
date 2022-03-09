'''
0128 Longest Consecutive Sequence 

start from a number x,
try examine x + 1, x + 2, ... , x + m in the set or not
obtain "the longest consecutive sequence" starting from x

How to optimize and avoid redundant operations?
1, 2, 3, 4,
1 + 1, 1 + 2, 1 + 3
2 + 1, 2 + 2
3 + 1,
Before checking x, examine if x - 1 in the set!
'''
# Straight forward
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)
        for num in nums:
            if num - 1 not in num_set:
                cur = 1
                curVal = num
                while curVal + 1 in num_set:
                    curVal += 1
                    cur += 1
                res = max(res, cur)
        return res
# Better Approach:
class Solution(object):
    def longestConsecutive(self, nums):
        hash_dict = dict()
        
        max_length = 0
        for num in nums:
            # hash_dict, key: number, 
            #            value: the length of consecutive sequence
            # Not in the hash_dict, need to update 
            if num not in hash_dict:
                # the 'dp' value of right number and left number
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                # add one -> current consecutive sequence length
                cur_length = 1 + left + right
                # update if larger than current max
                if cur_length > max_length:
                    max_length = cur_length
                # update the hash dict
                # Only if left & right exist can you update.
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                
        return max_length
'''
Method 2 Credit:
作者：jalan
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence/solution/dong-tai-gui-hua-python-ti-jie-by-jalan/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''