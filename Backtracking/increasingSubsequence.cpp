/**
0491 Increasing Subsequences
Backtracking + Pruning
*/
class Solution 
{
public:
    vector<int> running_vector;
    vector<vector<int>> result;
    
    void dfs(int cur, int lastElement, vector<int> &nums) 
    {
        if (cur == nums.size()) 
        {
            // Check if log the result
            if (running_vector.size() > 1) 
            {
                result.push_back(running_vector);
            }
            return;
        }
        // Append increasing elements
        // That is our rule for 'selecting' an element!
        if (nums[cur] >= lastElement) 
        {
            running_vector.push_back(nums[cur]);
            dfs(cur + 1, nums[cur], nums);
            running_vector.pop_back(); // Remember to pop
        }
        // Then, how about not selecting an element?
        // Do not duplicate, then consider not selecting.
        if (nums[cur] != lastElement) 
        {
            dfs(cur + 1, lastElement, nums);
        }
    }
    
    vector<vector<int>> findSubsequences(vector<int>& nums) 
    {
        dfs(0, INT_MIN, nums);
        return result;
    }
};