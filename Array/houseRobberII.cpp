/**
0213 House Robber II
We can divide the problem into 2 scenarios
1. Rob the first house, index from [0, N - 2]
2. Rob the last house, index from [1, N - 1]
Get the max of the two
*/

class Solution 
{
public:
    int robByRange(vector<int>& nums, int start, int end) 
    {
        int first = nums[start], second = max(nums[start], nums[start + 1]);
        for (int i = start + 2; i <= end; i++) 
        {
            int tmp = second;
            second = max(nums[i] + first, second);
            first = tmp;
        }
        return second;
    }
    
    int rob(vector<int>& nums) 
    {
        int num_houses = nums.size();
        if (num_houses == 1) 
        {
            return nums[0];
        }
        else if (num_houses == 2)
        {
            return max(nums[1], nums[0]);
        }
        else 
        {
            return max(robByRange(nums, 0, num_houses - 2), robByRange(nums, 1, num_houses - 1));
        }
    }
};