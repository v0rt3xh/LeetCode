/**
0278 First Bad Version
Binary Search
We want to set 'right': the last version that are not bad.
The ending condition of the loop: left <= right
Then, left is the version number we need.
*/

class Solution 
{
public:
    int firstBadVersion(int n) 
    {
        int left = 1, right = n;
        while (left <= right) 
        {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) 
            {
                // move right, when mid is bad version
                right = mid - 1;
            } else 
            {   // Otherwise, move left
                left = mid + 1;                
            }

        }
        // left is the result we need
        return left;
    }
};