'''
0096 Unique Binary Search Tree I
return the number of unique BSTs
'''

#### If we use the way in 0095: Exceed running time

class Solution:
    def numTrees(self, n: int) -> int:
        def buildTree(start, end):
            if start > end:
                return 1
            res = 0
            for i in range(start, end + 1):
                leftOptions = buildTree(start, i - 1)
                rightOptions = buildTree(i + 1, end)
                if leftOptions * rightOptions == 0:
                    res += leftOptions + rightOptions
                else:
                    res += leftOptions * rightOptions
            return res
        return buildTree(1, n)

#### DP approach

# LENGTH!!!!

### G(n): The number of unique BSTs with nodes sequence length n
### F(i, n), the count of unique BSTs which are rooted at i, length n 
### G(n) = sum_i F(i, n)
### G(0) = 1, G(1) = 1
# 1, 2, ... , i - 1, i, i + 1, ..., n
# F(i, n) = G(i - 1) * G (n - i)
# G(n) = sum_i G(i - 1) * G (n - i)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1) # dp matrix
        dp[0] = dp[1] = 1 # base cases
        for i in range(2, n + 1): # notice the range 2~n, 
                                  # as we expand the matrix dim by 1
            for k in range(1, i + 1): # the range, so true
                dp[i] += dp[k - 1] * dp[i - k]
        return dp[n]


