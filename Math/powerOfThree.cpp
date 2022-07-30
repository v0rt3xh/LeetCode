/**
0326 Power of Three
I thought we got even fancy methods.
*/

class Solution 
{
public:
    bool isPowerOfThree(int n) 
    {
        while (n && n % 3 == 0) 
        {
            n /= 3;   
        }
        return n == 1;
    }
};