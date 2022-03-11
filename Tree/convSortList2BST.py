'''
0109 Convert Sorted List to Binary Search Tree
Method 1, similar as 0108, we 'find' the median
Need a helper method to find median in a linked list
-> fast slow pointer
Also need a helper method to build the tree :)
'''
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def findMid(start, end):
            slow = fast = start
            while fast != end and fast.next != end:
                fast = fast.next.next
                slow = slow.next
            return slow
        
        def construct(start, end):
            if start == end:
                return None
            mid = findMid(start, end)
            node = TreeNode(mid.val)
            node.left = construct(start, mid)
            node.right = construct(mid.next, end)
            return node
        return construct(head, None)


'''
Improved method
'''
