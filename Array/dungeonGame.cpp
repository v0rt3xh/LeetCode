/**
0174 Dungeon Game
Dynamic programming, from bottom right to upper left
dp[i][j]: The shortest init value to save the princess, starting from i,j
dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
minimum value needed from the next step minus dungeon value,
remember, you need at least one life to proceed, thus, max(~, 1)
*/

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) 
    {
        int n = dungeon.size(), m = dungeon[0].size();
        // Corner case, set as INT_MAX
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, INT_MAX));
        dp[n][m - 1] = dp[n - 1][m] = 1; // Corner case, first iteration.
        for (int i = n - 1; i > -1; i--) 
        {
            for (int j = m - 1; j > -1; j--) 
            {
                int min_next = min(dp[i + 1][j], dp[i][j + 1]);
                dp[i][j] = max(min_next - dungeon[i][j], 1);
                    
            }
            
        }
        return dp[0][0];
    }
};