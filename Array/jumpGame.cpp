/**
0055 Jump Game
Wonderful Greedy
*/
class Solution 
{
public:
    bool canJump(vector<int>& nums) 
    {
        int length = nums.size();
        int maxJump = 0;
        for (int i = 0; i < length; i++) 
        {
            if (i > maxJump) 
            {
                // Cannot reach
                return false;
            }
            maxJump = max(maxJump, nums[i] + i);
        }
        return true;
    }
};