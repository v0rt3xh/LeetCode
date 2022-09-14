/**
0137 Single Number II
Iterative Solution
*/

class Solution 
{
public:
    int singleNumber(vector<int>& nums) 
    {
        int result = 0; 
        for (int i = 0; i < 32; i++) 
        {
            int total = 0;
            for (int num : nums) 
            {
                total += ((num >> i) & 1);
            } 
            if (total % 3) 
            {
                result |= (1 << i);
            }
        }
        return result;
    }
};

// finite state machine

class Solution 
{
public:
    int singleNumber(vector<int>& nums) 
    {
        int a = 0, b = 0;
        for (int num : nums) 
        {
            b = ~a & (b ^ num);
            a = ~b & (a ^ num);
        }
        return b;
    }
};