/**
 * 0414 The Third Maximum Number
 * Well, my sorting approach turns to be over complicated
 * 1. Sorting 2. Ordered set. 3. Three variables.
 */

class Solution1 {
public:
    int thirdMax(vector<int>& nums) 
    {
        sort(nums.begin(), nums.end());
        int target = 3;
        int prev;
        int i = nums.size() - 1;
        while (i > -1) 
        {
            if (i == nums.size() - 1) 
            {
                target -= 1;
                prev = nums[i];
                i--;
            }
            else 
            {
                while (i > -1 && nums[i] == prev) 
                {
                    i--;
                }
                if (i > -1) 
                {
                    target -= 1;
                    prev = nums[i];
                    i--;
                }
            }
            if (target == 0) 
            {
                return prev;
            }
        }
        return target == 0 ? prev : nums[nums.size() - 1];
    }
};


class Solution2 
{
public:
    int thirdMax(vector<int> &nums) 
    {
        set<int> s;
        for (int num : nums) 
        {
            s.insert(num);
            if (s.size() > 3) 
            {   // Erase smallest element
                s.erase(s.begin());
            }
        }
        return s.size() == 3 ? *s.begin() : *s.rbegin();
    }
};

// a, b, c, 1st largest, 2nd largest, 3rd largest
class Solution3 
{
public:
    int thirdMax(vector<int> &nums) 
    {
        long a = LONG_MIN, b = LONG_MIN, c = LONG_MIN;
        for (long num : nums) 
        {
            if (num > a) 
            {
                c = b;
                b = a;
                a = num;
            } else if (a > num && num > b) 
            {
                c = b;
                b = num;
            } else if (b > num && num > c) 
            {
                c = num;
            }
        }
        return c == LONG_MIN ? a : c;
    }
};