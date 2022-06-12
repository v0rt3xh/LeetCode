/**
0198 House Robber
dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
*/
class Solution 
{
public:
    int rob(vector<int>& nums) 
    {
        int N = nums.size();
        if (N == 1)
        {
            return nums[0];
        }
        int prior_2 = nums[0], prior_1 = max(nums[0], nums[1]);
        for (int i = 2; i < N; i++) 
        {
            int tmp = prior_1; 
            prior_1 = max(prior_2 + nums[i], prior_1);
            prior_2 = tmp;
        }
        return prior_1;
    }
};