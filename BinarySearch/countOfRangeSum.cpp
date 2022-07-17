/**
0327 Count of Range Sum
Prefix Sum + Merge Sort
Compute the prefix Sum -> PREFIX
For every index pair (i, j)
Finding the range < - > 
Find i, j such that PREFIX[j] - PREFIX[i] in [lower, upper]
======================
Suppose now we have two sorted ascending array A, B,
To find all the i, j such that B[j] - A[i] in [lower, upper],
We maintain 2 pointers l, r, both point to B[0] at first,
Consider A[0], 
we move l to the right, til B[l] - A[0] >= lower,
we move r to the right til B[r] - A[0] > upper
Thus all the indices j in [l, r) satisfy the range constraint.
======================
Consider A[1],
we just can only move l, r to right, since A is ascending.
Therefore, for each element in A,
we record the corresponding index pairs,
that yields the result.
*/

class Solution 
{
public:
    int countRangeSumRecursive(vector<long>& sum, int lower, int upper, int left, int right) 
    {
        if (left == right) 
        {
            // Stop the process
            return 0;
        } else 
        {
            // Divide step
            int mid = (left + right) / 2;
            int n1 = countRangeSumRecursive(sum, lower, upper, left, mid);
            int n2 = countRangeSumRecursive(sum, lower, upper, mid + 1, right);
            // Returned result
            int ret = n1 + n2;

            // Start point in A / A[0]
            int i = left;
            
            int l = mid + 1; // left, right at first point to the starting point of B / B[0].
            int r = mid + 1;
            while (i <= mid) 
            {
                // Constraint defined as aforementioned
                while (l <= right && sum[l] - sum[i] < lower) l++;
                while (r <= right && sum[r] - sum[i] <= upper) r++;
                ret += (r - l); // l - r is the count
                i++;
            }

            // Then merge the sorted array.
            vector<long> sorted(right - left + 1);
            int p1 = left, p2 = mid + 1;
            int p = 0;
            while (p1 <= mid || p2 <= right) 
            {
                if (p1 > mid) 
                {
                    sorted[p++] = sum[p2++];
                } else if (p2 > right) 
                {
                    sorted[p++] = sum[p1++];
                } else 
                {
                    if (sum[p1] < sum[p2]) 
                    {
                        sorted[p++] = sum[p1++];
                    } else 
                    {
                        sorted[p++] = sum[p2++];
                    }
                }
            }
            for (int i = 0; i < sorted.size(); i++) 
            {
                sum[left + i] = sorted[i];
            }
            return ret;
        }
    }

    int countRangeSum(vector<int>& nums, int lower, int upper) 
    {
        long s = 0;
        vector<long> sum{0};
        // Create prefix sum array
        for(auto& v: nums) 
        {
            s += v;
            sum.push_back(s);
        }
        // Start the divide and conquer step
        return countRangeSumRecursive(sum, lower, upper, 0, sum.size() - 1);
    }
};
/**
Credit：LeetCode-Solution
Link：https://leetcode.cn/problems/count-of-range-sum/solution/qu-jian-he-de-ge-shu-by-leetcode-solution/*/