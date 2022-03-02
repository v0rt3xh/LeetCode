'''
0124 Binary Tree Maximum Path Sum
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = float('-inf')
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # define a function maxGain to compute
        # starting from the node, its path's maximum path sum
        # Then, we create a variable to store current maxSum
        # curMax = max(curMax, leftGain + cur.val + rightGain)
        def maxGain(node):
            if not node:
                return 0
            # What do you mean by 0?
            # Only when gain is larger than 0, we select the leftnode
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            # currentPath, through the current node
            currentSum = leftGain + rightGain + node.val
            # update step
            self.maxSum = max(currentSum, self.maxSum)
            # magic! notice that we focus on the maxGain
            return node.val + max(leftGain, rightGain)
        maxGain(root)
        return self.maxSum