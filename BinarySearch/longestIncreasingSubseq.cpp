/**
0300 Longest Increasing Subsequence
Method 1 DP
dp[i] maximum length, ending with number[i].
dp[i] = max dp[j] + 1 for j < i and nums[j] < nums[i]
*/
class Solution1
{
public:
    int lengthOfLIS(vector<int>& nums) 
    {
        int length = nums.size();
        vector<int> dp_array(length, 0);
        int result = 0;
        for (int i = 0; i < length; i++) 
        {
            dp_array[i] = 1;
            for (int j = 0; j < i; j++) 
            {
                if (nums[j] < nums[i]) 
                {
                    dp_array[i] = max(dp_array[i], dp_array[j] + 1);
                }
            }
            result = max(dp_array[i], result);
        }
        return result;
    }
};

/**
0300 Longest Increasing Subsequence
Method 2 Binary Search
We want a subsequence that increase as slow as possible.
When we add a number to the end of current seq, want it small.
We then keep a array D[], 
D[i] stands for:
The smallest ending element in a subsequence of length i.
D[i] < D[j] for i < j, monotone.
We start from D[] with length 1, element: nums[0],
traverse through the array, suppose 
If nums[i] > D[len], D[len + 1] = nums[i]
Otherwise, search in D[],
find the element, say D[k] that is smaller than nums[i], set D[k + 1] to nums[i].
*/
class Solution2 
{
public:
    int lengthOfLIS(vector<int>& nums) 
    {
        // The length of D array.
        int length = 1, nums_length = nums.size();
        vector<int> D(nums_length + 1, 0);
        D[length] = nums[0];
        for (int i = 1; i < nums_length; i++) 
        {
            if (nums[i] > D[length]) 
            {
                D[++length] = nums[i];
            }
            else 
            {
                int left = 1, right = length, pos = 0;
                // Why pos 0? in case that current element is the smallest
                while (left <= right) 
                {
                    int mid = (left + right) >> 1;
                    if (D[mid] < nums[i]) 
                    {
                        pos = mid;
                        left = mid + 1;
                    }
                    else 
                    {
                        right = mid - 1;
                    }
                }
                D[pos + 1] = nums[i];
            }
        }
        return length;
    }
};