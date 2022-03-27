'''
0120 Triangle
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        dp = []
        for i in range(m):
            dp.append(0) # slow?
            # yeah, a lot of corner cases
            for j in range(i, -1, -1):
                if j == i:
                    dp[j] = dp[j - 1]
                elif j == 0:
                    dp[j] = dp[j]
                else:
                    dp[j] = min(dp[j], dp[j - 1])
                dp[j] += triangle[i][j]
        return min(dp)
'''
Better Style and Neater approach
'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            # the right end case
            f[i] = f[i - 1] + triangle[i][i]
            # bellman equation
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            # the left end case
            f[0] += triangle[i][0]
        
        return min(f)
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/triangle/solution/san-jiao-xing-zui-xiao-lu-jing-he-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''