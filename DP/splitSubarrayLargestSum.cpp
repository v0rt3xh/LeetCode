/**
0410 Split Array Largest Sum
1. DP approach,
DP[i][j], The smallest "largest sum" obtained by 
Dividing the first i elements into j subarrays.
DP[i][j] = min_{k = 0}^{i - 1} (max(DP[k][j - 1], subSum(k + 1, i)))
subSum: the sum of elements in the given range.
Valid state must have i >= j.
We can assign invalid states' values to INF.
Corner case:
DP[0][0] is 0.
*/

class Solution1 
{
public:
    int splitArray(vector<int>& nums, int m) 
    {
        int length = nums.size();
        // DP Array Init
        vector<vector<long long>> DP(length + 1, vector<long long>(m + 1, LLONG_MAX));
        // Range sum (prefix sum)
        vector<long long> prefix(length + 1, 0);
        for (int i = 0; i < length; i++) 
        {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        DP[0][0] = 0;
        for (int i = 1; i <= length; i++) 
        {
            for (int j = 1; j <= min(i, m); j++) 
            {
                for (int k = 0; k < i; k++) 
                {
                    DP[i][j] = min(DP[i][j], max(DP[k][j - 1], prefix[i] - prefix[k]));
                }
            }
        }
        return (int) DP[length][m];
    }
};

/**
0410 Split Array Largest Sum
2. Binary Search
*/

class Solution {
public:
    bool check(vector<int>& nums, int x, int m) {
        long long sum = 0;
        int cnt = 1;
        for (int i = 0; i < nums.size(); i++) {
            if (sum + nums[i] > x) {
                cnt++;
                sum = nums[i];
            } else {
                sum += nums[i];
            }
        }
        return cnt <= m;
    }

    int splitArray(vector<int>& nums, int m) {
        long long left = 0, right = 0;
        for (int i = 0; i < nums.size(); i++) {
            right += nums[i];
            if (left < nums[i]) {
                left = nums[i];
            }
        }
        while (left < right) {
            long long mid = (left + right) >> 1;
            if (check(nums, mid, m)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};
/**
Credit：LeetCode-Solution
Link：https://leetcode.cn/problems/split-array-largest-sum/solution/fen-ge-shu-zu-de-zui-da-zhi-by-leetcode-solution/
*/

