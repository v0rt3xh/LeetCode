/**
 * 0152 Maximum Product Subarray
 * DP, but two DP 'array'
 * 
 */


class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int max_cursor, min_cursor; // stands for dp_min array, dp_max array.
        // dp_max[i], max product we can have in the array ending with num[i]
        // similar defined for min
        max_cursor = nums[0];
        min_cursor = nums[0];
        int res = nums[0]; // stores result
        int tmp; // swapping helper
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] >= 0) {
                // Current element negative
                max_cursor = max(max_cursor * nums[i], nums[i]);
                min_cursor = min(min_cursor * nums[i], nums[i]);
            }
            else {
                // Do not forget that in cpp, swapping elements not like Python
                tmp = max_cursor;
                max_cursor = max(min_cursor * nums[i], nums[i]);
                min_cursor = min(tmp * nums[i], nums[i]);
            }
            res = max(res, max_cursor);    
        }
        return res;
    }
};