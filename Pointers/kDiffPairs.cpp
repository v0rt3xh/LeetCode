/**
0532 K-diff Pairs in An Array
Method 1. Hash set
We use two hash sets.
First set: 
    Store result, we use the smaller element in each pair as marker.
Second set:
    Store the element we have seen.
*/

class Solution1 
{
public:
    int findPairs(vector<int>& nums, int k) 
    {
        unordered_set<int> visited;
        unordered_set<int> result; 
        for (int num: nums) 
        {
            if (visited.count(num - k)) 
            {
                result.emplace(num - k);
            }
            if (visited.count(num + k)) 
            {
                result.emplace(num);
            }
            visited.emplace(num);
        }
        return result.size();
    }
};

/**
 * Method 2 
 * Sorting & Two pointers
 * Notice k >= 0
 * left, right == 0 (init)
 */

class Solution2 
{
public:
    int findPairs(vector<int>& nums, int k) 
    {
        sort(nums.begin(), nums.end());
        int length = nums.size(), result = 0, ptr2 = 0;
        // Traverse by ptr1
        for (int ptr1 = 0; ptr1 < length; ptr1++) 
        {
            if (ptr1 == 0 || nums[ptr1] != nums[ptr1 - 1]) 
            {
                while (ptr2 < length && (nums[ptr2] < nums[ptr1] + k || ptr2 <= ptr1)) 
                {
                    ptr2++;
                }
                if (ptr2 < length && nums[ptr2] == nums[ptr1] + k) 
                {
                    result++;
                }
            }
        }
        return result;
    }
};

