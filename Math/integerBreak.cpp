/**
0343 Integer Break
- Math Solution
Want to split the number into divisor in 3's if possible
-> mod 3 = 0: just 3^quotient
-> mod 3 = 1: 1 * 3 < 2 * 2: 3^(quotient - 1) * 4
-> mod 3 = 2: 3^(quotient) * 2
*/
class Solution 
{
public:
    int integerBreak(int n) 
    {
        if (n <= 3) 
        {
            return n - 1;
        }
        int quotient = n / 3, remainder = n % 3;
        if (remainder == 0) 
        {
            return (int)pow(3, quotient);
        }
        else if (remainder == 1) 
        {
            return (int)pow(3, quotient - 1) * 4;
        }
        else 
        {
            return (int)pow(3, quotient) * 2;    
        }
    }
};