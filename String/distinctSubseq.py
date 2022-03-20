'''
0115 Distinct Subsequences
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0 
        m, n = len(s), len(t)
        # Dynamic Programming
        '''
        dp[i][j]: In s[i:], the number of occurrence of t[j: ]
        Boundary Case: 
                      dp[m][k] = 0, k < n, s[m:] is ''
                      dp[l][n] = 1, t[n:] is ''
        Bellman Equation:
        For i < m, j < n:
            1. s[i] == t[j]:
               1.1 Add s[i] to the working path, check dp[i + 1][j + 1]
               1.2 Do not add s[i] to the working path, check dp[i + 1][j]
               e.g, baaaaggggg & bag, meet the first a, include it or not.
            2. s[i] != t[j]:
               Cannot choose s[i], has to be dp[i + 1][j]
        dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j], s[i] == t[j]
        dp[i][j] = dp[i + 1][j], s[i] != t[j]
        '''
        # init, we consider 0 ~ m, 0 ~ n. Thus + 1 dimension
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        return dp[0][0]
'''
Credit:
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
来源：力扣（LeetCode）
'''