'''
0102 Binary tree level order traversal
Classic BFS, with len(queue) as a helper
How to improve it?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS approach
        if not root:
            return []
        # resulting list
        res = []
        # the working queue
        queue = [root]
        while queue:
            tmp = [] # tmp storage
            for i in range(len(queue)):
                element = queue.pop(0)
                tmp.append(element.val)
                # current element's neighbors
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            res.append(tmp)
        return res
        