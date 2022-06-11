/**
0382 Linked List Random Node
Reservoir sampling?
Start from the head,
For the i-th node we just visited, 
We sample a number from [0, i)
If the number is zero, 
we set our return value to i-th node's value
*/
class Solution {
    ListNode* head;
public:
    Solution(ListNode* head) {
        this->head = head; 
    }
    
    int getRandom() {
        int i = 1, ans = 0;
        for (auto node = head; node; node = node->next) 
        {
            if (rand() % i == 0) 
            {
                ans = node->val;
            }
            ++i;
        }
        return ans;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */