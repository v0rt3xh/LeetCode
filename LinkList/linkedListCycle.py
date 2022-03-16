'''
0141 Linked List Cycle
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Very basic Idea, hash set to store the nodes
        which takes O(N) space
        '''
        storage = set()
        cursor = head
        while cursor:
            if cursor in storage:
                return True
            storage.add(cursor)
            cursor = cursor.next
        return False
'''
Better method, use pointers.
Fast / slow ptrs.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast:
            slow = slow.next
            fast = fast.next
            # fast pointer move twice
            if fast:
                fast = fast.next
            else:
                break
            if fast == slow:
                return True
        return False
        