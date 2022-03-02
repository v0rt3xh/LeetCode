'''
0061 Rotate List
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = 
# Shitty solution ....
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        sentinel = ListNode(next=head)
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        rotateIndex = length - k % length
        # rotateIndex is the new 'end'
        # rotateIndex.next is the new 'head'
        if rotateIndex == 0:
            return head
        cur = head
        for _  in range(rotateIndex - 1):
            cur = cur.next
        # cur now is the new end
        sentinel.next = cur.next
        newHead = cur.next
        if not newHead:
            return head
        cur.next = None
        while newHead.next:
            newHead = newHead.next
        newHead.next = head
        return sentinel.next

# Try a neater one, credit: Leetcode-cn
# Create a ring,
# suppose length is n
# Notice that the (n - 1) - k mod n ^th node is the 'end' (start from 0)
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head
        # get the length
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        
        # add => n - k % n
        # do nothing
        if (add := n - k % n) == n:
            return head
        # cur: current end
        # create a ring
        cur.next = head
        # Find the break point
        while add:
            cur = cur.next
            add -= 1
        # ret is the new head
        # cur: the new end
        ret = cur.next
        cur.next = None
        return ret