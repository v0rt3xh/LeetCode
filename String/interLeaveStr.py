'''
0097 Interleaving String
Resemble 'Path'! Walk through the string, to obtain the gold.
dp[i, j]: The first i element of s1 and first j element of s2,
          can interleave to the first i + j element of s3.
For the index of s1, s2, s3, we start counting from 0. 
When s1[i - 1] (i.e, i-th element) == s3[i + j - 1] (i + j-th element)
    dp[i - 1, j] is what we are looking for
Similarly, when s2[j - 1] == s3[i + j -1],
    dp[i, j - 1] is what we are looking for
Thus,
    dp[i, j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1] ) 
                or
               (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
Init / corner case
    dp[0, 0] = True
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Dynamic programming at its finest
        '''
        n, m, t = len(s1), len(s2), len(s3)
        # if length not match, just False
        if n + m != t:
            return False
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        # initialize the dp matrix / corner cases
        for i in range(1, n + 1):
            dp[i][0] =  dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                tail = i + j - 1
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[tail]) or (dp[i][j - 1] and s2[j - 1] == s3[tail]) 
        return dp[-1][-1]