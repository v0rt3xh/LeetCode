/**
0260 Single Number III
Bit manipulation
xor to the end,
must be x (xor) y!
x (xor) y is not 0, there must be a digit, 
where x, y should differ.
Suppose it's the k-th digit,
We can divide the numbers in nums into two categories.
*/
class Solution 
{
public:
    vector<int> singleNumber(vector<int>& nums) 
    {
        int xor_sum = 0;
        for (int num: nums) 
        {
            xor_sum ^= num;
        }
        // Get the lowest 1 of xor_sum
        // Prevent overflow
        int lowest_one = (xor_sum == INT_MIN ? xor_sum : xor_sum & (-xor_sum));
        int category1, category2 = 0;
        for (int num: nums) 
        {
            if (num & lowest_one) 
            {
                category1 ^= num;
            }    
            else 
            {
                category2 ^= num;
            }
        }
        return {category1, category2};
    }
};