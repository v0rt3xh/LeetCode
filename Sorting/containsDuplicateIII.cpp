/**
0220 Contains Duplicate III
Sliding Window + Ordered Set
*/
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) 
    {
        int length = nums.size();
        set<int> storage;
        for (int i = 0; i < length; i++) 
        {
            // Do not want to get out of int
            // Introduce INT_MIN and INT_MAX
            auto iter = storage.lower_bound(max(nums[i], INT_MIN + t) - t);
            if (iter != storage.end() && *iter <= min(nums[i], INT_MAX - t) + t)
            {
                // Find a number satisfies the condition
                return true;
            }
            storage.insert(nums[i]);
            if (i >= k) 
            {
                // Control the size of sliding window
                storage.erase(nums[i - k]);
            }
            
        }
        return false;
    }
};