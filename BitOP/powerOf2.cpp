/**
0231 Power of Two
For numbers that are power of two,
we must have n & (n - 1) == 0
*/

class Solution 
{
public:
    bool isPowerOfTwo(int n) 
    {
        return n > 0 && (n & (n - 1)) == 0;
    }
};