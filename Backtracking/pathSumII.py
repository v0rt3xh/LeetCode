'''
0113 Path Sum II
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = list()
        if not root:
            return res
        def backtrack(node, target, path):
            '''
            If met a leaf node, check if the target is satisfied.
            '''
            if not node.left and not node.right:
                if target - node.val == 0:
                    path.append(node.val)
                    res.append(path[:])
                    path.pop()
                return
            '''
            Otherwise, add to current path
            '''
            path.append(node.val)
            '''
            start left / right when not None
            '''
            if node.left:
                backtrack(node.left, target - node.val, path)
            if node.right:
                backtrack(node.right, target - node.val, path)
            # Remove current element
            path.pop()
        backtrack(root, targetSum, [])
        return res