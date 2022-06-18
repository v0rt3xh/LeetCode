/**
0268 Missing Number
1. Math
2. Bit manipulation xor
*/

class Solution1 
{
public:
    int missingNumber(vector<int>& nums) 
    {
        int N = nums.size();
        int sum_of_nums = accumulate(nums.begin(), nums.end(), 0);
        return N * (N + 1) / 2 - sum_of_nums;
    }
};