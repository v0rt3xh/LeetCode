/**
0121 Best Time to Buy And Sell Stock
*/


class Solution 
{
public:
    int maxProfit(vector<int>& prices) 
    {
        int result = 0, curMin = INT_MAX;
        for (int price : prices) 
        {
            if (price < curMin) 
            {
                curMin = price;
            }
            else 
            {
                result = max(result, price - curMin);
            }
        }
        return result;
    }
};