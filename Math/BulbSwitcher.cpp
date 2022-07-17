/**
0319 Bulb Switcher
1, 2, 3, ... n bulbs,
k-th bulb's # of toggles:
    The number of k's divisors.
Even number of divisor: Off
Odd number of divisor: On
k / x must appears the same time as x,
Then, when x^2 != k,
That divisor will appear even times
So we are finding k that are square numbers.
return lower_bound{sqrt(n)}
*/

class Solution 
{
public:
    int bulbSwitch(int n) 
    {
        // Guarantee precision
        return sqrt(n + 0.5);
    }
};