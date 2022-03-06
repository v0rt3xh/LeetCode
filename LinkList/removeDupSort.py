'''
0083 Remove Duplicates from Sorted List
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
        '''
        My approach does not use sentinel
        pos: insert position
        cur: cursor to travel through the list
        '''
        pos = head
        cur = head
        # record current value
        curVal = head.val
        while cur:
            # if repeated, just skip
            while cur and cur.val == curVal:
                cur = cur.next
            # catenate to the insert position
            pos.next = cur
            # move the position pointer
            pos = pos.next
            # No way to go, stop
            if not cur:
                break
            # otherwise, update value
            curVal = cur.val
            # move cursor
            cur = cur.next
        return head

'''
Or, just one pointer
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
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                # remove cur.next
                cur.next = cur.next.next
            else:
                # move cursor
                cur = cur.next
        return head