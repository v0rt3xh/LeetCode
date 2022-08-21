/**
0503 Next Greater Element II
One traversal is not enough.
Concatenate a copy to the end. (module index to achieve this.)
Notice that we only need first (length - 1) elements
*/
class Solution 
{
public:
    vector<int> nextGreaterElements(vector<int>& nums) 
    {
        int length = nums.size();
        vector<int> result(length, -1);
        stack<int> working_stack;
        for (int i = 0; i < 2 * length - 1; i++) 
        {
            while(!working_stack.empty() && nums[working_stack.top()] < nums[i % length]) 
            {
                result[working_stack.top()] = nums[i % length];
                working_stack.pop();
            }
            working_stack.push(i % length);
        }
        return result;
    }
};