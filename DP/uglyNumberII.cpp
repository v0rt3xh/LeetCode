/**
0264 Ugly Number II
2 3 5 corresponding pointers p2, p3, p5
dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
Then move the pointer by 1
*/
class Solution 
{
public:
    int nthUglyNumber(int n) 
    {
        vector<int> dp_array(n + 1, 0);
        dp_array[1] = 1;
        int p2 = 1, p3 = 1, p5 = 1;
        for (int i = 2; i < n + 1; i++) 
        {
            int num2 = dp_array[p2] * 2, num3 = dp_array[p3] * 3, num5 = dp_array[p5] * 5;
            dp_array[i] = min(min(num2, num3), num5);
            if (num2 == dp_array[i]) 
            {
                p2++;
            }
            if (num3 == dp_array[i]) 
            {
                p3++;
            }
            if (num5 == dp_array[i]) 
            {
                p5++;
            }
        }
        return dp_array[n];
    }
};