'''
0098 validate BST
 My first attempt was a greedy approach
 which was ... pretty bad
 keep max ? min root
 Need extra parameters...
 Current min and current max??
 So each step,
 we need to compare the root value with min and max
 Also start the recursive step at its child
 This thought helps us determine the syntax of our recursive method.
 recurish(min, max, node)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # One thing important
        # Though you may satisfy the local condition,
        # It's hard to tell if it would work globally
        def recur(node, maxVal=float('inf'), minVal=float('-inf')):
            # Null: return True
            if not node:
                return True
            curVal = node.val
            # Not satisfying global max and min: return False
            if curVal >= maxVal or curVal <= minVal:
                return False
            # Start the recursive steps.
            return recur(node.left, curVal, minVal) and recur(node.right, maxVal, curVal)
        return recur(root)
        
