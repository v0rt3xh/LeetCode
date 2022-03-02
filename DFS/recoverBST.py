'''
0099 recoverBST
in which order, can we reserve the property of BST?
-inorder
put them in a list
-find the positions that have the wrong order
note that from our analysis
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Store the nodes
        nodes = []
        # Define inorder
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)
        # i, j for potential positions
        i = None
        j = None
        # Now the tricky part 
        start = nodes[0]
        for k in range(1, len(nodes)):
            if nodes[k].val < start.val:
                j = nodes[k]
                if not i:
                    i = start
            start = nodes[k]
        if i and j:
            i.val, j.val = j.val, i.val
        
        