'''
0025 Reverse Nodes in k-Group
It reminds me of reversing linked list.
Two parts.
First: 
    we need to determine if there is a group of length k,
    only when the group is of length k,
    we reverse the group.
Second:
    reverse!
    need a reverse function for sub linked lists
    Given head and tail of a sub linked list,
    return the reversed head and tail
'''

class Solution:
    # First, write a sub function -> reverse a subLinkedList
    def reverse(self, head, tail):
        # To understand this part,
        # We better draw a picture
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
            # tail now is head, head now is tail
        return tail, head
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Start from the beginning,
        # We need to check if the group length >= k
        # If it is, then swap.
        # Notice that, we need to alter the connections at the two ends!
        # Set a sentinel to help us:
        hair = ListNode(0)
        hair.next = head
        pre = hair
        while head:
            tail = pre
            # Check if we got a length > k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            # store the next group, help us catenate
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            # that pre cursor really helps us catenate the first half
            pre = tail
            head = tail.next
        return hair.next

'''
Credit: https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/k-ge-yi-zu-fan-zhuan-lian-biao-by-leetcode-solutio/
A bit summary:
    sentinel really helps,
    prev pointer needed
    (In this case), we need 'head, tail' & a 'next' as well
'''
