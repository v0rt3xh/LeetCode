'''
0441 Arranging Coins
Exist k such that k * (k + 1) / 2 = n 
I choose plain iteration, quite slow.
Binary Search is much faster.
'''
class Solution1:
    def arrangeCoins(self, n: int) -> int:
        result = 1
        while result * (result + 1) - 2 * n <= 0:
            result += 1
        return result - 1 


# Math method
class Solution2:
    def arrangeCoins(self, n: int) -> int:
        return int((pow(8 * n + 1, 0.5) - 1) / 2)

# Binary Search, notice the computation of mid
class Solution3:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right + 1) // 2
            if mid * (mid + 1) - 2 * n <= 0:
                left = mid
            else:
                right = mid - 1
        return left