'''
0070 Climbing Stairs
Classic DP
f(n) = f(n - 1) + f(n - 2)
f(0) = 1, f(1) = 1
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            b, a = a + b, b
        return b
