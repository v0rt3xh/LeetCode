/**
0421 Maximum XOR of Two Numbers in An Array
For XOR, 
If a ^ b = c; Then b ^ c = a, c ^ a = b
We must have a maximum result for this problem.
We don't need to know which two numbers lead to our result. 

-We want the number to be large enough. 
-1 needs to appear in higher digits.
-So, we can start from the highest digit, check if it's possible to make it 0

Say a ^ b leads to max: x.
Then, we must have max ^ b = a.

*/

class Solution 
{
public:
    int findMaximumXOR(vector<int>& nums) 
    {
        int N = nums.size();
        int res = 0;
        int mask = 0; // Use mask to retrieve prefix
        for(int j = 31; j >= 0; j--) 
        {
            // Constant range: 32 digits
            // Check every digit 
            // Current prefix mask
            mask = mask | (1 << j);
            unordered_set<int> dp;
            // It serves as a hash set for each digit
            // First assume that we may choose 1 on current digit.
            int temp = res | (1 << j);
            for(int i = 0; i < N; i++) 
            {
                // Find if it's possible to set current digit to 1
                // Found in the hash set, then we can!
                if (dp.find((nums[i] & mask)^temp) != dp.end()) 
                {
                    res = temp;
                    break;
                } else 
                {
                    // Not found, insert possible prefix values
                    dp.insert(nums[i] & mask);
                }
            }
        }
        return res;        
    }
};
