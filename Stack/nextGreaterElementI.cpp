/**
0496 Next Greater Element I 
Monotone Stack
Move from right to left (nums2),
maintain a monotone stack
Hashtable store result
*/
class Solution 
{
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) 
    {
        unordered_map<int, int> reference; 
        stack<int> working_stack;
        for (int i = nums2.size() - 1; i > -1; i--) 
        {
            while (!working_stack.empty() && working_stack.top() < nums2[i]) 
            {
                working_stack.pop();
            }
            reference[nums2[i]] = working_stack.empty() ? -1 : working_stack.top();
            working_stack.push(nums2[i]);
        }
        vector<int> result(nums1.size());
        for (int i = 0; i < nums1.size(); i++) 
        {
            result[i] = reference[nums1[i]];
        }
        return result;
    }
};