/** 
 * 0374 Guess Number Higher or 
   Binary Search
 */

class Solution {
public:
    int guessNumber(int n) 
    {
        int left = 1, right = n;
        while (left < right) 
        {   
            int mid = left + (right - left) / 2; // Prevent overflow
            int guess_flag = guess(mid);
            if (guess_flag == 0) 
            {
                return mid;
            }
            else if (guess_flag == 1) 
            {
                left = mid + 1;
            }
            else 
            {
                right = mid - 1;
            }
        }
        return left;
    }
};