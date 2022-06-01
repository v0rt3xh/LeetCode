/**
 * 0328 Odd Even Linked List
 * Introduce an sentinel node (or just start with head.next)
 * odd & even pointer, traverse through the linked list
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        // Special case
        if (head == nullptr) {
            return head;
        }
        ListNode* evenHead = head->next;
        ListNode* odd = head;
        ListNode* even = head->next;
        while (even != nullptr && even->next != nullptr) {
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even = even->next;
        }
        odd->next = evenHead;
        return head;
    }
};