/**
0275 H-Index II
When doing binary search, we can also return value based on
'left' and 'right', not just 'mid'!
*/

class Solution {
public:
    int hIndex(vector<int>& citations) 
    {
        int n = citations.size();
        int left = 0, right = n - 1;
        while (left <= right) 
        // Find the boundary!
        // At the end:
        // H-index possible | H-index Not possible
        // left | left + 1, ..., end 
        {
            int mid = left + (right - left) / 2;
            // The rule of this binary search:
            if (citations[mid] >= n - mid) 
            {
                right = mid - 1;
            }
            else 
            {
                left = mid + 1;
            }
        }
        return n - left;
    }
};
