/**
0283 Move Zeroes
*/
class Solution 
{
public:
    void moveZeroes(vector<int>& nums) 
    {
        int cursor = 0;
        int length = nums.size();
        for (int i = 0; i < length; i++) 
        {
            if(nums[i] != 0) 
            {
                nums[cursor++] = nums[i];
            }
        }
        for (int i = cursor; i < length; i++) 
        {
            nums[i] = 0;
        }
    }
};

class Solution2 
{
public:
    void moveZeroes(vector<int>& nums) 
    {
        int left = 0;
        for (int right = 0; right < nums.size(); right++) 
        {
            if (nums[right] != 0) 
            {
                int tmp = nums[left];
                nums[left++] = nums[right];
                nums[right] = tmp;
            }
        }
    }
};