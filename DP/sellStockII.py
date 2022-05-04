'''
0122 Best Time to Buy and Sell Stock II
Key to Fortune 
'''
'''
dp approach:
2 states: Holding a stock at day i or not
dp[i][0]: maximum profit possible when not holding a stock on day i
dp[i][1]: ~ but holding a stock on day i
dp[i][0] = max{dp[i - 1][0], dp[i - 1][1] + price[i]}
dp[i][1] = max{dp[i - 1][1], dp[i - 1][0] - price[i]}
Here:
    +: sell it, add up our balance 
    -: purchase stock, use our balance
result: dp[n - 1][0]
In the code, the dp matrix got transposed though. 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i - 1], dp[1][i - 1] + prices[i])
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1] - prices[i])
        return dp[0][n - 1]


'''
Greedy Approach
Find k disjoint intervals (l_i, r_i]
such that sum_{i=1}^{k} price[r_i] - price[l_i] -> maximized 
Factorized into sub-interval with length 1
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            if prices[i] >= prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res

