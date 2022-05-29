/*
0217 Contains Duplicate
*/

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> container;
        for (int num: nums) {
            if (container.find(num) != container.end()) {
                return true;
            }
            container.insert(num);
        }
        return false;
    }
};