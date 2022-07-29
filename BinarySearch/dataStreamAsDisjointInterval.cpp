/**
0352 Data Stream as Disjoint Intervals
Ordered Mapping
For a given value, we first find the smallest l1 such that
                        l1 > val. With interval [l1, r1];
Then find the largest l0 such taht l0 <= val,
                        with interval [l0, r0]
Case 1 to 5
1: l0 <= val <= l1
2: r0 + 1 = val
3: l1 - 1 = val
4: r0 + 1 = val && l1 - 1 =val
5: Escape case
*/
class SummaryRanges 
{
private:
    map<int, int> intervals;

public:
    SummaryRanges() {}
    
    void addNum(int val) 
    {
        // Find the interval
        auto interval1 = intervals.upper_bound(val);
        auto interval0 = (interval1 == intervals.begin() ? intervals.end() : prev(interval1));

        if (interval0 != intervals.end() && interval0->first <= val && val <= interval0->second) 
        {
            // Case 1 do nothing
            return;
        }
        else 
        {
            bool left_aside = (interval0 != intervals.end() && interval0->second + 1 == val);
            bool right_aside = (interval1 != intervals.end() && interval1->first - 1 == val);
            if (left_aside && right_aside) 
            {
                // case 4 
                int left = interval0->first, right = interval1->second;
                intervals.erase(interval0);
                intervals.erase(interval1);
                intervals.emplace(left, right);
            }
            else if (left_aside) 
            {
                // Case 2
                ++interval0->second;
            }
            else if (right_aside) 
            {
                // Case 3
                int right = interval1->second;
                intervals.erase(interval1);
                intervals.emplace(val, right);
            }
            else 
            {
                // Case 5, just [val, val]
                intervals.emplace(val, val);
            }
        }
    }
    
    vector<vector<int>> getIntervals() 
    {
        vector<vector<int>> ans;
        for (const auto& [left, right]: intervals) 
        {
            ans.push_back({left, right});
        }
        return ans;
    }
};
/**
Credit：LeetCode-Solution @ Leetcode.cn
Link：https://leetcode.cn/problems/data-stream-as-disjoint-intervals/solution/jiang-shu-ju-liu-bian-wei-duo-ge-bu-xian-hm1r/
*/