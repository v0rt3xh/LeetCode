/**
0315 Count of Smaller Numbers After Self
Index array + Merge Sort
Credit: newlewis @ leetcode-cn
*/

class Solution 
{
public:
    vector<int> res;

    vector<int> countSmaller(vector<int>& vec) 
    {

        if (vec.empty())
        {
            return {};
        }
        // Index Array
        vector<pair<int, int>> nums;
        for (int i = 0; i < vec.size(); i++)
        {
            // First: element, second: index    
            nums.emplace_back(vec[i], i);
        }

        res = vector<int>(vec.size(), 0);
        // Merge sort on index array
        merge_sort(nums, 0, (int)nums.size() - 1);

        return res;
    }

    void merge_sort(vector<pair<int, int>>& nums, int left, int right)
    {
        // Divide step
        if (left < right)
        {
            int mid = left + (right - left) / 2;

            merge_sort(nums, left, mid);
            merge_sort(nums, mid + 1, right);
            merge(nums, left, mid, right);
        }
    }

    void merge(vector<pair<int, int>>& nums, int left, int mid, int right)
    {
        int i = left, j = mid + 1;
        int k = left;
        // Auxiliary tool, store interim results
        vector<pair<int, int>> sort_nums;

        while (i <= mid && j <= right)
        {
            if (nums[i].first <= nums[j].first)
            {
                // Add to the corresponding location in res
                // using the index array.
                res[nums[i].second] += j - mid - 1;
                sort_nums.push_back(nums[i++]); // append nums[i], then++
            }
            else if (nums[i].first > nums[j].first)
            {
                sort_nums.push_back(nums[j++]);
            }
        }
        // Remaining items
        while (i <= mid)
        {   // Larger than any element to the right of mid
            res[nums[i].second] += j - mid - 1;
            sort_nums.push_back(nums[i++]);
        }

        while (j <= right){
            sort_nums.push_back(nums[j++]);
        }

        for (int m = 0, n = left; m < sort_nums.size(); m++, n++)
        {
            nums[n] = sort_nums[m];
        }
    }
};