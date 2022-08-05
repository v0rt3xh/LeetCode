/**
 * 0725
 * First get length, 
 * Then get the quotient and remainder 
 * -> to determine the length of splits
 */
class Solution 
{
public:
    vector<ListNode*> splitListToParts(ListNode* head, int k) 
    {
        ListNode* cursor = head;
        int length = 0;
        while (cursor != nullptr) 
        {
            cursor = cursor->next;
            length += 1;
        }
        int init_length = length / k, add_on = length % k;
        vector<ListNode*> result(k, nullptr);
        cursor = head;
        for (int index = 0; index < k && cursor != nullptr; index++) 
        {
            result[index] = cursor;
            int current_length = init_length + (index < add_on ? 1 : 0);
            for (int i = 1; i < current_length; i++) 
            {
                cursor = cursor->next;
            }
            ListNode* tmp = cursor->next;
            cursor->next = nullptr;
            cursor = tmp;
        }
        return result;
    }
};