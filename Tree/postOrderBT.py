'''
0145 Binary Tree Postorder Traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Recursive step
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def recur(node):
            if not node:
                return
            recur(node.left)
            recur(node.right)
            res.append(node.val)
        recur(root)
        return res
'''
Simulate the implicit stack
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        callStack = []
        prev = None # Very important, helps us avoid Infite recursion
        while root or callStack:
            # first append all the 'left' children
            while root:
                callStack.append(root)
                root = root.left
            # Okay, check right children
            root = callStack.pop()
            # does not have right children, 
            # or we have processed the right children
            # append the value, set prev as root,
            # root => None
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                # do have, then append back to stack
                # we need to process the remaining stuffs
                callStack.append(root)
                root = root.right
        return res