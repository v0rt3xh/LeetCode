'''
0538 Convert BST to Greater Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Retrieve the reverse order of the BST nums' list
        '''
        def recur(node):
            if not node:
                return
            recur(node.right)
            queue.append(node)
            recur(node.left)
        '''
        Use a queue to update the values，
        Then, a natural question: why bother using a explicit queue??
        '''
        queue = deque()
        recur(root)
        val = 0
        while queue:
            node = queue.popleft()
            tmp = node.val
            node.val += val
            val += tmp
        return root

'''
A simpler version
Credit: Leetcode-cn
'''
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recur(node):
            nonlocal total
            if node:
                recur(node.right)
                total += node.val
                node.val = total
                recur(node.left)
        total = 0
        recur(root)
        return root
            