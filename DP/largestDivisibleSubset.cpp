/**
0368 Largest Divisible Subset
Dynamic Programming.
Sort the distinct positive integers set first. 

- If integer a is the divisor of the smallest element in subset A,
  then we can append a to subset A & increase the size.
  Similarly, if interger b is the multiple of the largest element in subset B,
  then we can append b to subset B.
  
- dp[i]: The size of the largest subset we can get, if choosing nums[i] as the largest
number in that subset. (Assuming that we have sorted nums in an ascending order.)
*/

class Solution 
{
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) 
    {
        // Preprocess 
        int length = nums.size();
        sort(nums.begin(), nums.end());
        
        // init DP array, values should be 1 (the default size of a subset)
        vector<int> dp(length, 1);
        // Now we find the size of the largest subset & the correponding max number
        // Why max number? Help us to retrieve the set.
        int maxSize = 1;
        int maxVal = dp[0];
        for (int i = 1; i < length; i++) 
        {
            for (int j = 0; j < i; j++) 
            {
                if (nums[i] % nums[j] == 0) 
                {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            if (dp[i] > maxSize) 
            {
                maxSize = dp[i];
                maxVal = nums[i];
            }
            
        }
        
        // Retrieve the set.
        vector<int> result;
        // Special case
        if (maxSize == 1) 
        {
            result.push_back(nums[0]);
            return result;
        }
        // reverse traversal.
        // meet maxSize, check if we can append (% == 0)
        // add the number, reduce size, change maxVal
        for (int i = length - 1; i > -1 && maxSize > 0; i--) 
        {
            if (dp[i] == maxSize && maxVal % nums[i] == 0) 
            {
                result.push_back(nums[i]);
                maxSize--;
                maxVal = nums[i];
            }
        }
        return result;
    }
};