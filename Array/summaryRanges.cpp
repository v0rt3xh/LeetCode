/**
0228 Summary Ranges
Rules & Iteration 
*/

class Solution 
{
public:
    vector<string> summaryRanges(vector<int>& nums) 
    {
        int length = nums.size();
        int cursor = 0;
        vector<string> result;
        while (cursor < length) 
        {
            int prev = nums[cursor];
            while ((cursor + 1 < length) && (nums[cursor] + 1 == nums[cursor + 1])) 
            {
                cursor += 1;
            }
            if (prev != nums[cursor]) 
            {
                result.push_back(to_string(prev) + "->" + to_string(nums[cursor]));
                cursor += 1;
            }
            else 
            {
                result.push_back(to_string(prev));
                cursor += 1;
            }
        }
        return result;      
    }
};