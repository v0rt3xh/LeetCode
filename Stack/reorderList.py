'''
0143 Reorder List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Well, try better approaches. 
Mine kinda ...
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the mid point
        # A genius would use fast & slow pointers though
        # slow = slow.next
        # fast = fast.next.next 
        # That was ... amazing
        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        mid = count // 2
        # Split the linked list into two halves
        # right half inverse!
        # I use a stack to complete this
        stack = []
        cur = head
        i = 0
        while cur:
            if i >= mid:
                stack.append(cur)
            cur = cur.next
            i += 1
        # merge step
        cur = head
        while stack:
            tmp = cur.next
            node = stack.pop()
            # sometimes the split incurs some troubles
            # so have to exclude some 'loops'
            if cur == node or tmp == node:
                break
            node.next = tmp
            cur.next = node
            if stack:
                # remember to remove current stack top's next
                stack[-1].next = None
            cur = tmp
        return head

'''
Pro's Approach
'''
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp
