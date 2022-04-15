'''
0669 Trim Binary Search Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        left, right subtrees， low, high is the same
        For left subtree, if root.val < low
            root = recur(root.right)
            elif root.val >= low and root.val <= high:
                root.left = recur(root.left)
                root.right = recur(root.right)
            elif root.val > high:
                root = recur(root.left)
        Recursive way, it takes some space,
        Can we improve it? Need to simulate the implicit stack,
                           Or define a helper method,
                           then we don't have to pass-in low, high!
        '''
        if not root:
            return None
        if root.val < low:
            root = self.trimBST(root.right, low, high)
        elif root.val <= high and root.val >= low:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        else:
            root = self.trimBST(root.left, low, high)
        return root

'''
Credit: Leetcode-cn 
Solution Verison
'''
class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)