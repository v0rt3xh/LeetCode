'''
0257 Binary Tree Paths
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        '''
        Path, auxiliary array method,
        use "->" to concatenate the strings when appending.
        If current node: a leaf node, concatenate the string and store
        If current node has a left child or right child, recur, 
        ** Remember to pop the values of child nodes **
        '''
        def recur(node, path):
            # Notice that root in this case [1, 100]
            # So would be reasonable to neglect empty root case.
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append("->".join(path))
                return
            if node.left:
                recur(node.left, path)
                path.pop()
            if node.right:
                recur(node.right, path)
                path.pop()
        res = []
        path = []
        recur(root, path)
        return res