/**
0445 Add Two Numbers II
Use a stack to store the elements, 
Then, add it up.
 */
class Solution 
{
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        stack<int> stack1, stack2;
        // Get those digits
        while (l1) 
        {
            stack1.push(l1->val);
            l1 = l1->next;
        }
        while (l2) 
        {
            stack2.push(l2->val);
            l2 = l2->next;
        }
        int digit = 0; 
        ListNode *result = nullptr;
        // Start to add up
        while (digit or !stack1.empty() or !stack2.empty()) 
        {
            int first_num = stack1.empty() ? 0 : stack1.top();
            int second_num = stack2.empty() ? 0: stack2.top();
            if (!stack1.empty()) stack1.pop();
            if (!stack2.empty()) stack2.pop();
            int addup = first_num + second_num + digit;
            // Pay attention to our operations on node
            auto node = new ListNode(addup % 10);
            digit = addup / 10;
            // node -> next = result ensures the order
            node->next = result;
            result = node;
        }
        return result;
    }
};