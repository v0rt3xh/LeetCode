/**
0376 Wiggle Subsequence
DP approach,
essentially maintain 2 * length(nums) DP array
DP_up[i]: The longest wiggle subsequence ending with an element
          in the range of [0, i]. And the last two elements are 'increasing'
=============
DP_down[i]: The longest wiggle subsequence ending with an element in [0, i]
            And the last two elements are 'decreasing'
=============
DP_up[i] =  DP_up[i - 1] -> nums[i - 1] >= nums[i]
            max(DP_up[i - 1], DP_down[i - 1] + 1) -> nums[i - 1] < num[i]
DP_down[i] = DP_down[i - 1] -> nums[i - 1] <= nums[i]
             max(DP_down[i - 1], DP_up[i - 1] + 1) -> nums[i - 1] > num[i]
*/
class Solution 
{
public:
    int wiggleMaxLength(vector<int>& nums) 
    {
        int length = nums.size();
        if (length < 2) 
        {
            return length;
        }
        int up = 1, down = 1;
        for (int i = 1; i < length; i++) 
        {
            if (nums[i] > nums[i - 1]) 
            {
                up = max(up, down + 1);
            }
            else if (nums[i] < nums[i - 1])
            {
                down = max(down, up + 1);
            }
        }
        return max(up, down);
    }
};