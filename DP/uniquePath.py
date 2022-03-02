'''
0062 Unique Paths
'''
'''
# 1 Math solution, of course
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = m + n - 2
        choose = min(m - 1, n - 1)
        if choose == 0:
            return 1
        denom = 1
        numer = 1
        while choose:
            denom *= choose
            choose -= 1
            numer *= steps
            steps -= 1
        return int(numer / denom)

'''
Sort of DP stuff
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp =[[0] * n for _ in range(m)]
        dp[0][0] = 1 
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
        return dp[m - 1][n - 1]
