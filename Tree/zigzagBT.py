'''
0103 Binary Tree Zigzag Level Order Traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # I have seen you before lmao
        if not root:
            return 
        queue = [root]
        # Add a swag switch
        # Any smarter move?
        swag = 1
        res = []
        while queue:
            curLevel = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                curLevel.append(node.val)
            if swag == -1:
                curLevel = curLevel[::-1]
            swag *= -1
            res.append(curLevel)
        return res