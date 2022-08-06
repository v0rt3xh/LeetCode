/**
041 First Missing Positive
Use array as the hashTable.
Suppose len(array) = N
The missing positive could only be in the range
[1, N + 1]
1. Set all negatives to N + 1
2. Hashing 
3. Traverse and get the result. 
*/
class Solution 
{
public:
    int firstMissingPositive(vector<int>& nums) 
    {
        int length = nums.size();
        for (int& num: nums) 
        {
            if (num <= 0) 
            {
                num = length + 1;
            }
        }
        for (int i = 0; i < length; i++) 
        {
            int number = abs(nums[i]);
            if (number < length + 1) 
            {
                nums[number - 1] = -abs(nums[number - 1]);
            }
        }
        for (int i = 0; i < length; i++) 
        {
            if (nums[i] > 0) 
            {
                return i + 1;
            }
        }
        return length + 1;
    }
};