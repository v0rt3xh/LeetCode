'''
0086 Partition List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # My first thought was manipulating in-place ...
        # two sentinels
        # the first one catenate the nodes that have values < x
        # the second catenate the nodes that have values >= x
        sentinel1, sentinel2 = ListNode(), ListNode()
        cur = head
        cur1 = sentinel1
        cur2 = sentinel2
        while cur:
            if cur.val < x:
                cur1.next = cur
                cur1 = cur1.next
            else:
                cur2.next = cur
                cur2 = cur2.next
            cur = cur.next
        # Important step
        # catenate the ends
        # remember to set cur2.next as None
        cur1.next = sentinel2.next
        cur2.next = None
        return sentinel1.next