/**
0349 Intersection of Two Arrays 
Two hash sets
*/

class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) 
    {
        // build the set
        unordered_set<int> set1, set2;
        for (auto& num: nums1) 
        {
            set1.insert(num);
        }
        for (auto& num: nums2)
        {
            set2.insert(num);
        }
        return getIntersection(set1, set2);
    }
    
    vector<int> getIntersection(unordered_set<int>& set1, unordered_set<int>& set2) 
    {
        // Iterate through the smaller set
        if (set1.size() > set2.size()) 
        {
            return getIntersection(set2, set1);
        }
        vector<int> intersections;
        for (auto& num : set1) 
        {
            if (set2.count(num)) 
            {
                intersections.push_back(num);
            }
        }
        return intersections;
    }
};