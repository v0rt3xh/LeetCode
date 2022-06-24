/**
0338 Counting Bits
For a number x, 
we have digit[x] = digit[y] + 1
where y has the same number of as x, except the top digit.
Thus, we need to find a number z, 
such that z is the maximum power of 2, s.t. z <= x.
Good property: for a positive integer, (m & (m - 1)) == 0 if power of 2.

*/
class Solution 
{
public:
    vector<int> countBits(int n) 
    {
        vector<int> result(n + 1, 0);
        int current_power = 0;
        for (int i = 1; i < result.size(); i++) 
        {
            if (!(i & (i - 1))) 
            {
                current_power = i;
            }
            result[i] = result[i - current_power] + 1;
        }
        return result;
    }
};