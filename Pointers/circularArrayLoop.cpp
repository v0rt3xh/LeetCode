/**
0457 Circular Array Loop
Slow, Fast pointers 
Set traversed elements as 0! Wow.
Credit: LeetCode CN solution
*/
class Solution 
{
public:
    bool circularArrayLoop(vector<int>& nums) 
    {
        int n = nums.size();
        
        // Define a helper method to get next position. 
        auto next = [&] (int cur) 
        {
            return ((cur + nums[cur]) % n + n) % n;
        };
        
        for (int i = 0; i < n; i++) 
        {
            if (!nums[i]) 
            {
                // We set 0 for traversed elements.
                continue;
            }
            int slow = i, fast = next(i);
            while (nums[slow] * nums[fast] > 0 && nums[slow] * nums[next(fast)] > 0) 
            {
                if (slow == fast) 
                {   // Make sure not having cycle with length 1
                    if (slow != next(slow)) 
                    {
                        return true;
                    }
                    else 
                    {
                        break;
                    }
                }
                slow = next(slow);
                fast = next(next(fast));
            }
            int visited = i;
            // Mark visited as 0
            while (nums[visited] * nums[next(visited)] > 0) 
            {
                int tmp = visited;
                visited = next(visited);
                nums[tmp] = 0;
            }
        }
        return false;
    }
};
