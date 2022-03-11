'''
0144 Binary Tree Preorder Traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Recursive Step
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        def recur(node):
            if not node:
                return
            res.append(node.val)
            recur(node.left)
            recur(node.right)
        recur(root)
        return res

'''
Iterative
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [] # simulate stack
        res = [] # result list
        node = root # "working" node
        while stack or node:
            while node: # node exist
            `   # pre order, first append value
                res.append(node.val)
                # add to the stack
                stack.append(node)
                # left first
                node = node.left
            # then deal with the right part!
            # the order is perfectly-constrained by the stack.
            node = stack.pop()
            node = node.right
        return res
