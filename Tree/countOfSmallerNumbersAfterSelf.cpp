/**
0315 Count of Smaller Numbers After Self
Binary Indexed Tree
Credit: LeetCode-Solution @ leetcode-cn
*/

class Solution {
private:
    vector<int> c;
    vector<int> a;

    void Init(int length) {
        c.resize(length, 0);
    }

    int LowBit(int x) {
        return x & (-x);
    }

    void Update(int pos) {
        while (pos < c.size()) {
            c[pos] += 1; // Update prefixSum
            pos += LowBit(pos);
        }
    }

    int Query(int pos) {
        int ret = 0;

        while (pos > 0) { // Compute the count
            ret += c[pos];
            pos -= LowBit(pos);
        }

        return ret;
    }

    void Discretization(vector<int>& nums) {
        a.assign(nums.begin(), nums.end());
        sort(a.begin(), a.end());
        // Remove duplicate elements.
        // There would some indeterminate items, need to cut them off.
        a.erase(unique(a.begin(), a.end()), a.end());
    }
    
    int getId(int x) {
        // Query Id
        return lower_bound(a.begin(), a.end(), x) - a.begin() + 1;
    }
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> resultList;

        Discretization(nums);

        Init(nums.size() + 5);
        
        for (int i = (int)nums.size() - 1; i >= 0; --i) {
            int id = getId(nums[i]); // Mapping
            resultList.push_back(Query(id - 1)); // Get result
            Update(id);
        }

        reverse(resultList.begin(), resultList.end());

        return resultList;
    }
};