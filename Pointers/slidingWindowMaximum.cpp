/**
0239 Sliding Window Maximum
Sliding window + monotone queue
*/
class Solution 
{
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) 
    {
        int length = nums.size();
        deque<int> monoQueue;
        // init the first window.
        for (int i = 0; i < k; i++) 
        {
            while (!monoQueue.empty() && nums[monoQueue.back()] <= nums[i]) 
            {
                monoQueue.pop_back();
            }
            monoQueue.push_back(i);
        }
        vector<int> result;
        result.push_back(nums[monoQueue.front()]);
        // Now we start the full process. 
        for (int right = k; right < length; right++) 
        {
            while(!monoQueue.empty() && nums[right] >= nums[monoQueue.back()]) 
            {
                monoQueue.pop_back();
            }
            monoQueue.push_back(right);
            while(monoQueue.front() <= right - k) 
            {
                monoQueue.pop_front();
            }
            result.push_back(nums[monoQueue.front()]);
        }
        return result;
    }
};