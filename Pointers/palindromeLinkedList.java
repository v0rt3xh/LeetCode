/*
0234 Palindrome Linked List
*/

/**
We can convert the linked list -> array, string + two pointers
Let's check a reverse linked list approach.

 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        // Exclude special case
        if(head == null || head.next == null) {
            return true;
        }
        // slow, fast pointer
        ListNode slow = head, fast = head;
        // auxiliary variable for swapping the node
        ListNode pre = head, prepre = null;
        while(fast != null && fast.next != null) {
            pre = slow;
            // slow, fast pointer move like usual
            slow = slow.next;
            fast = fast.next.next;
            // at the same time,
            // use slow ptr to swap.
            pre.next = prepre;
            prepre = pre;
        }
        // This is for odd length linked list
        // move to the element after oddPivot 
        // left - oddPivot - right
        if(fast != null) {
            slow = slow.next;
        }
        // Now, use pre, the reversed list's head
        // And slow, to check if palindrome
        while(pre != null && slow != null) {
            if(pre.val != slow.val) {
                return false;
            }
            pre = pre.next;
            slow = slow.next;
        }
        return true;
    }
/*
Credit:
作者：nuan
链接：https://leetcode-cn.com/problems/palindrome-linked-list/solution/wo-de-kuai-man-zhi-zhen-du-cong-tou-kai-shi-gan-ju/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。*/
}