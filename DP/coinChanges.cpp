/**
 * 0322 Coin Change
 * 
 */

class Solution {
    // Dynamic Programming Approach
    // F(i): smallest number of coins needed for amount i
    // F(i) = min F(i - C_j) {j = 1, 2, ... C} + 1
public:
    int coinChange(vector<int>& coins, int amount) 
    {
        int MAX = amount + 1;
        vector<int> dp(amount + 1, MAX);
        dp[0] = 0;
        for (int i = 1; i <= amount; i ++)
        {
            for (int j = 0; j < coins.size(); j++) 
            { 
                if (coins[j] <= i) {
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
};