'''
0121 Best Time to Buy And Sell Stock
'''
'''
Straight forward
Behind the scene: Monotonic Stack
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = float('-inf')
        minPrice = prices[0]
        for p in prices:
            res = max(res, p - minPrice)
            minPrice = min(minPrice, p)
        return res
'''
Buffett's method
'''