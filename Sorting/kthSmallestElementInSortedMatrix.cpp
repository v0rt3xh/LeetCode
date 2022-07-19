/**
0378 Kth Smallest Element in a Sorted Matrix
Binary Search Approach
Credit: Leetcode Solution
Can also be done in sorting approach
Merge sort + heap
*/
class Solution 
{
public:
    bool checkAmount(vector<vector<int>> &matrix, int mid, int k, int n) 
    {
        // Starting from the left lower corner.
        int i = n - 1;
        int j = 0;
        // Count how many numbers are smaller than mid
        int count = 0;
        while (i > -1 and j < n) 
        {
            if (matrix[i][j] <= mid) 
            {
                count += i + 1;
                // the column of index i all smaller than mid
                j++;
            }
            else 
            {
                // need to get to lower place
                i--;
            }
        }
        return count >= k;
    }
    
    int kthSmallest(vector<vector<int>>& matrix, int k) 
    {
        int n = matrix.size();
        int left = matrix[0][0];
        int right = matrix[n - 1][n - 1];
        while (left < right) 
        {
            int mid = left + ((right - left) >> 1);
            if (checkAmount(matrix, mid, k, n)) 
            {
                // more than k, set right -> mid
                right = mid;
            }
            else 
            {
                // less than k, need to increase left value
                left = mid + 1;
            }
        }
        return left;
    }
};