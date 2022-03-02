'''
0019 remove N-th node from end of List
fast slow pointer???
also sentinel trick
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode(next=head) # Add a sentinel
        fast = sentinel
        slow = sentinel
        prev = sentinel # Record connection
        for i in range(n):
            fast = fast.next # Let the fast one go first
        while fast: # if fast is NONE, time to delete!
            prev = slow
            fast = fast.next
            slow = slow.next
        prev.next = slow.next
        return sentinel.next