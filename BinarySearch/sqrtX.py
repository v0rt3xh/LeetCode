'''
0069 sqrt(x)
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        left = 1
        right = x
        while left <= right:
            mid = (right + left) // 2
            if mid * mid < x:
                left = mid + 1
            if mid * mid > x:
                right = mid - 1
            if mid * mid == x:
                return mid
        return right

# Newton's method lmao