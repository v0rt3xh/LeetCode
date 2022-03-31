'''
0201 Bitwise AND of Numbers Range
Need more practice on bit operations.
'''
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # Find the common prefix
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift
'''
e.g: 
    9: 0 0 0 0 1 0 0 1
   12: 0 0 0 0 1 1 0 0
   shift = 3
   m: at the common prefix,
      left shift 3 times to retrieve the result
    ---------------------
    1: 0 0 0 0 0 0 0 1
    1: 0 0 0 0 0 0 0 1
    shift = 0
'''

'''
Credit
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/solution/shu-zi-fan-wei-an-wei-yu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''