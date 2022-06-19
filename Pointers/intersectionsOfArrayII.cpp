/**
0350 Intersection of Two Arrays II
Solution 1, Hashmap, 
store number of times that an element appear.
Could take up too much space.
Solution 2, sort + double pointers
Credit: Leetcode Solution - CN
*/

class Solution 
{
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) 
    {
        // first sort the two arrays
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        int length1 = nums1.size(), length2 = nums2.size();
        vector<int> intersection; // return intersection as result
        int index1 = 0, index2 = 0;
        while (index1 < length1 && index2 < length2) 
        {
            if (nums1[index1] < nums2[index2]) 
            {   // move the smaller element's pointer
                index1++;
            } else if (nums1[index1] > nums2[index2]) 
            {
                index2++;
            } else {
                intersection.push_back(nums1[index1]);
                index1++;
                index2++;
            }
        }
        return intersection;
    }
};
/**
Credit：LeetCode-Solution
Link：https://leetcode.cn/problems/intersection-of-two-arrays-ii/solution/liang-ge-shu-zu-de-jiao-ji-ii-by-leetcode-solution/
*/