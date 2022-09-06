/**
 * 0082 Remove Duplicates from Sorted List II
 cpp version
 */
class Solution 
{
public:
    ListNode* deleteDuplicates(ListNode* head) 
    {
        if (head == nullptr || head->next == nullptr) 
        {
            return head;
        }
        ListNode* sentinel = new ListNode();
        sentinel->next = head;
        ListNode* pre = sentinel;
        ListNode* cur = sentinel->next;
        while (cur != nullptr) 
        {
            while (cur->next != nullptr && cur->val == cur->next->val) 
            {
                cur = cur->next;
            }
            // Important part comes in
            if (pre->next == cur) 
            {
                pre = pre->next;
            }
            else 
            {
                pre->next = cur->next;
            }
            cur = cur->next;
        }
        return sentinel->next;
    }
};