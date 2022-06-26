/**
 * 0258 Add Digits
 * Well, that's impressive.
 * Number = sum_{i = 0}^{n} a_i * 10 ^ i
 *        = sum_{i = 0}^{n} a_i + sum_{i = 0}^{n} a_i * (10^i - 1)
 *  Then, okay, just mod 9. 
 *  0 & 9's multiples are special cases. 
 */
class Solution 
{
public:
    int addDigits(int num) 
    {
        if (num == 0) 
        {
            return 0;
        }
        if (num % 9 == 0) 
        {
            return 9;
        }
        return num % 9;
    }
};