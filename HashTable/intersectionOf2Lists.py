'''
0160 Intersection of Two Linked Lists
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Maintain two pointers
if intersect, 
headA 
    a distinct nodes
                     c common nodes
    b distinct nodes
headB
just ptr1 -> if none, then points to headB
     ptr2 -> if none, then points to headA

In the end, they both walk 'a + b + c'!    
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1, ptr2 = headA, headB
        # if ptr1 reach none, move it to headB
        # if ptr2 reach none, move it to headA
        while ptr1 != ptr2:
            ptr1 = ptr1.next if ptr1 else headB
            ptr2 = ptr2.next if ptr2 else headA
            # will terminate, when both of them -> None
        return ptr1