'''
0082 Remove Duplicates from Sorted List II
Get quite puzzled on this one
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        sentinel = ListNode()
        sentinel.next = head
        cur = sentinel
        # next 2 nodes
        while cur.next and cur.next.next:
            # Find duplicates
            if cur.next.val == cur.next.next.val:
                # record the value
                curVal = cur.next.val
                # delete the nodes
                while cur.next and cur.next.val == curVal:
                    # this is the 'delete' script
                    cur.next = cur.next.next
            else:
                # otherwise, just move forward
                cur = cur.next
        return sentinel.next
