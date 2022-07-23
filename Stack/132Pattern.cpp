/**
0456 132 Pattern
Monotone Stack
Suppose the pattern is (i, j, k)
Enumerate 'i'
Reversely traverse
*/

class Solution 
{
public:
    bool find132pattern(vector<int>& nums) 
    {
        int length = nums.size();
        stack<int> candidate_k;
        candidate_k.push(nums[length - 1]);
        int max_k = INT_MIN;
        for (int i = length - 2; i > -1; i--) 
        {
            if (nums[i] < max_k) 
            {
                return true;
            }
            while (!candidate_k.empty() && candidate_k.top() < nums[i]) 
            {
                max_k = candidate_k.top();
                candidate_k.pop();
            }
            if (nums[i] > max_k) 
            {
                candidate_k.push(nums[i]);
            }
        }
        return false;
    }
};