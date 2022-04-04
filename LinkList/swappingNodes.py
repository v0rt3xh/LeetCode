'''
April Challenge
1721 Swapping Nodes in a Linked List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, second = head, head
        for _ in range(k - 1):
            second = second.next
        # Find the first k-th Node
        tmp = second
        # proceed to retrieve the last k-th node
        second = second.next
        while second:
            first = first.next
            second = second.next
        first.val, tmp.val = tmp.val, first.val
        return head
        