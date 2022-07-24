/**
0494 Target Sum
Backtrack / DP
*/
// 1. Backtrack
class Solution1
{
public:
    int count = 0;
    // We need: the number array, current index, current sum, and target
    void dfs(vector<int> &nums, int index, int sum, int target) 
    {
        if (index == nums.size()) 
        {   // Check if we can add up count
            if (sum == target) 
            {
                count++;
            }
        } else 
        {   // dfs step
            dfs(nums, index + 1, sum - nums[index], target);
            dfs(nums, index + 1, sum + nums[index], target);
        }
    }
    
    int findTargetSumWays(vector<int>& nums, int target) 
    {
        dfs(nums, 0, 0, target);
        return count;
    }
};

/**
2. DP approach,
suppose the numbers add up to SUM
set as negative's elements add up to NEG
set as positive's elements add up to POS
SUM - NEG = POS
(SUM - NEG) - NEG = target (that expression)
NEG = (SUM - target) / 2 -> rule out SUM - target : even case.
==============================
Thus, now we are selecting elements from nums, such that
their values add up to NEG: Knapsack problem
Recall DP[i][j], # of ways: 
                 select first i items in the knapsack, 
                 such that their values add up to j
DP[n][NEG] -> result
DP[0][0]: 1, DP[0][~0]: 0
Transition:
    dp[i][j] = dp[i - 1][j] if nums[i] > j
    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i]] if nums[i] <= j

*/
class Solution2
{
public:
    int findTargetSumWays(vector<int>& nums, int target) 
    {
        int sum = 0;
        for (int &num: nums) 
        {
            sum += num;
        }
        // Rule out special cases
        if ((sum - target) < 0 || (sum - target) % 2 != 0) 
        {
            return 0;
        }
        int negative = (sum - target) / 2;
        int n = nums.size();
        vector<vector<int>> dp(n + 1, vector<int>(negative + 1));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) 
        {
            int current_num = nums[i - 1];
            for (int j = 0; j <= negative; j++) 
            {
                dp[i][j] = dp[i - 1][j];
                if (j >= current_num) 
                {
                    dp[i][j] += dp[i - 1][j - current_num];
                }
            }
        }
        return dp[n][negative];
    }
};