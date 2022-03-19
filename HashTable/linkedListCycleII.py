'''
0142 Linked List Cycle II
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast != slow:
            return 
        # No, the key part, find the starting node
        # Trick:
        '''
        After we observe fast == slow,
        we move slow ptr to head and 'step by step'!
        When slow, fast first encouter, 
            1. l_{slow} * 2 = l_{fast}
            Here, l stands for the length they have walked.
            2. l_{fast} = l_{slow} + n * R
            Here, n is an integer, R is the ring length.
            Thus, l_{slow} = n * R, l_{fast} = 2n * R
        '''
        slow = head
        '''
        Now, reset l_{slow} = 0,
        Suppose it takes m step to reach the starting node
        We want to see l_{slow} = m 
                       l_{fast} = m + 2n * R
        They should meet at the starting node, if we 'step by step'.
        '''
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
'''
Credit: Krahets @LeetCode-CN
'''