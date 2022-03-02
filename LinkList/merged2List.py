'''
0021 Merge two sorted linked list
iterative approach is easy
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        cur = sentinel
        ptr1 = list1
        ptr2 = list2
        while ptr1 or ptr2:
            if not ptr1:
                cur.next = ptr2
                break
            if not ptr2:
                cur.next = ptr1
                break
            if ptr1.val <= ptr2.val:
                cur.next = ptr1
                ptr1 = ptr1.next
            else:
                cur.next = ptr2
                ptr2 = ptr2.next
            cur = cur.next
        return sentinel.next

### recursive approach

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: # empty 1, just return 2
            return list2
        if not list2: # empty 2, just return 1
            return list1
        if not list1 and not list2: # empty
            return None
        if list1.val <= list2.val: # smaller l1, keep it 
            # start recursive step @ l1 
            list1.next = self.mergeTwoLists(list1.next, list2)
            # Gotta return dude!
            return list1
        else: # smaller l2, keep it 
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2