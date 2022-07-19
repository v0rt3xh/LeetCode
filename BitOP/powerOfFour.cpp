/**
0342 Power of Four
1. Loop
2. Bit Operation:
Check if power of two & % 3 == 1
*/

class Solution 
{
public:
    bool isPowerOfFour(int n) 
    {
        return n >= 0 && (n & (n - 1)) == 0 && n % 3 == 1;   
    }
};