'''
0050 power(x, n)
Fast power =D
Divide and Conquer
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def divideAndConquer(value):
            # Base: value -> 0 return 1
            if value == 0:
                return 1
            sub = divideAndConquer(value // 2)
            # odd or even
            if value % 2 == 0:
                return sub * sub
            else:
                return x * sub * sub
        if n >= 0:
            return divideAndConquer(n)
        else: # divide by 1
            return 1.0 / divideAndConquer(-n)
