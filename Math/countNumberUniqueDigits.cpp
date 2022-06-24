/**
0357  Count Number with Unique Digits
Combinatorics
Remember to add previous digits' result
For instance:
n = 2:
9 * 9 + 10 (10 from n = 1's result)
*/

class Solution 
{
public:
    int countNumbersWithUniqueDigits(int n) 
    {
        if (n == 0) 
        {
            return 1;
        }
        if (n == 1) 
        {
            return 10;
        }
        // e.g. before 3-digit, we have 2-digit
        // Put them in 'previous_digit'
        // By the end, we will return it as the answer.
        // current is computed as 9 * (9 * 8 *....*(9 - n + 2))
        int previous_digit = 10, current = 9;
        for (int i = 0; i < n - 1; i++) 
        {
            current *= 9 - i;
            previous_digit += current;
        }
        return previous_digit;
    }
};