'''
0110 Balanced Binary Tree

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recur(node):
            # Empty -> Balanced
            if not node:
                return (0, True)
            # recursive step for left
            right, rightBool = recur(node.right)
            left, leftBool = recur(node.left)
            # larger than 1 differences, false 
            if abs(right - left) <= 1:
                # make sure use leftBool and rightBool
                return (max(left, right) + 1, leftBool and rightBool)
            else:
                return (max(left, right) + 1, False)
        
        _, res = recur(root)
        return res

#OR 

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
