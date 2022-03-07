'''
0112 Path Sum
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Empty node, just false
        if not root:
            return False
        # Leaf node, check our target
        if not root.left and not root.right:
            return targetSum - root.val == 0
        # otherwise, check left or right children
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum -root.val)
        