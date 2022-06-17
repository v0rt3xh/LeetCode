/**
0229 Majority Element II 
1. Hash table + 
2. Boyer-Moore Majority Vote
*/

class Solution1 
{
public:
    vector<int> majorityElement(vector<int>& nums) 
    {
        int n = nums.size();
        vector<int> result;
        unordered_map<int, int> counter;
        for (auto &value: nums) 
        {
            counter[value]++;
        }
        
        for (auto &element: counter) 
        {
            if (element.second > n / 3) 
            {
                result.push_back(element.first);
            }
        }
        return result;
    }
};

class Solution2 
{
// Bayer-Moore, you count two elements!
// the remaining two, are the candidates
public:
    vector<int> majorityElement(vector<int>& nums) 
    {
        vector<int> result;
        int element1 = 0, element2 = 0;
        int vote1 = 0, vote2 = 0;
        for (auto& num: nums) 
        {   // First 2 cases:
            // We have assigned two candidates.
            // And they match with current number.
            if (vote1 > 0 && num == element1) 
            {
                vote1++;
            } 
            else if (vote2 > 0 && num == element2) 
            {
                vote2++;
            }
            // Next 2: 
            // Vote is 0, should change candidate!
            else if (vote1 == 0) 
            {
                element1 = num;
                vote1++;
            }
            else if (vote2 == 0)
            {
                element2 = num;
                vote2++;
            }
            // Otherwise, both do not match
            // reduce both
            else 
            {
                vote1--;
                vote2--;
            }
        }
        // Then, determine what to include in outputs.
        int count1 = 0, count2 = 0;
        for (auto &num: nums) 
        {   // must have vote > 0 to be possible
            if (vote1 > 0 && num == element1) 
            {
                count1++;
            }
            if (vote2 > 0 && num == element2) 
            {
                count2++;
            }
        }
        if (vote1 > 0 && count1 > nums.size() / 3) 
        {
            result.push_back(element1);
        }
        if (vote2 > 0 && count2 > nums.size() / 3) 
        {
            result.push_back(element2);            
        }
        return result;
    }
};