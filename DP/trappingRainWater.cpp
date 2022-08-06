/**
 * 0042 Trapping Rain Water 
 * DP approach, Stack approach, and two pointers.
 * 
 */



class Solution1 
{
    // DP solution
public:
    int trap(vector<int>& height) 
    {
        int result = 0;
        int length = height.size();
        vector<int> leftDP(length), rightDP(length);
        leftDP[0] = height[0];
        rightDP[length - 1] = height[length - 1];
        for (int i = 1; i < length; i++) 
        {
            leftDP[i] = max(height[i], leftDP[i - 1]);
        }
        for (int j = length - 2; j > -1; j--) 
        {
            rightDP[j] = max(height[j], rightDP[j + 1]);
        }
        for (int i = 1; i < length - 1; i++) 
        {
            result += min(leftDP[i], rightDP[i]) - height[i];
        }
        return result;   
    }
};

class Solution2 
{
    // Stack solution
public:
    int trap(vector<int>& height) 
    {
        int result = 0, cursor = 0;
        stack<int> working_stack;
        while (cursor < height.size()) 
        {
            while (!working_stack.empty() && height[working_stack.top()] < height[cursor]) 
            {
                int current_top = working_stack.top();
                working_stack.pop();
                if (working_stack.empty()) 
                {
                    break;
                }
                int distance = cursor - working_stack.top() - 1;
                int curHeight = min(height[working_stack.top()], height[cursor]) - height[current_top];
                result += distance * curHeight;
            }
            working_stack.push(cursor++); // push, then move to the next position 
        }
        return result;

    }
};

class Solution3 
{
    // pointers solution
public:
    int trap(vector<int>& height) 
    {
        int left = 0, right = height.size() - 1;
        int result = 0;
        int leftMax = 0, rightMax = 0;
        while (left < right) 
        {
            if (height[left] < height[right]) 
            {
                height[left] >= leftMax ? (leftMax = height[left]) : result += (leftMax - height[left]);
                left++;
            }
            else 
            {
                height[right] >= rightMax ? (rightMax = height[right]) : result += (rightMax - height[right]);
                right--;
            }
        }
        return result;
    }
};