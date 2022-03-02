'''
0107 Binary Tree Level Order Traversal II

'''
# Silly Approach 1
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        stack = [root]
        while stack:
            curRes = []
            curLevel = len(stack)
            for i in range(curLevel):
                node = stack.pop(0)
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    curRes.append(node.val)
            if curRes:
                res.insert(0, curRes)
        return res
# CAUTION: reverse a list is more efficient than insert from the head in Python.