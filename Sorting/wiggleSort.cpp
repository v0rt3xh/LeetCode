/**
0324 Wiggle Sort II
Worth review,
many other solutions,
this time submit the plainest one.
Sort & divide the array from mid point
mid point index = floor(nums_length + 1 / 2) - 1
This is for the odd length case 
want the last element smaller than previous element.
nums[mid_index], nums[nums_length - 1], nums[mid_index - 1], nums[nums_length - 2]
...
nums[0], nums[mid_index + 1] (Even case)

*/
class Solution 
{
public:
    void wiggleSort(vector<int>& nums) 
    {
        int nums_length = nums.size();
        vector<int> tool = nums;
        sort(tool.begin(), tool.end());
        int mid_index = (nums_length + 1) / 2 - 1;
        for (int i = 0, j = mid_index, k = nums_length - 1; i < nums_length; i += 2, j--, k--) 
        {
            nums[i] = tool[j];
            if (i + 1 < nums_length) 
            {
                nums[i + 1] = tool[k];
            }
        }
        
    }
};