/**
0219 Contains Duplicate II
Sliding window and Hashset
The sliding window has a length k + 1
Therefore, the difference between numbers <= k
*/
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> storage;
        int length = nums.size();
        for (int i = 0; i < length; i++) 
        {
            if (i > k) 
            {
                // Control the length of hashset 
                storage.erase(nums[i - k - 1]);
            }
            if (storage.count(nums[i])) 
            {
                return true;
            }
            storage.emplace(nums[i]);
        }
        return false;
    }
};