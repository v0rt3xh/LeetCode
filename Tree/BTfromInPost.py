'''
0106 Construct Binary Tree from Inorder and Postorder Traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def recur(current, left, right):
            '''
            current: current root / node 's index in the postorder list 
            left: left boundary of the left subtree
            right: right boundary of the right subtree
            '''
            if left > right: # exceed the boundary, just quit
                return 
            curVal = postorder[current] # curVal serves as the hashkey
            curNode = TreeNode(curVal)
            # build the right subtree
            curNode.right = recur(current - 1, hashSet[curVal] + 1,right) 
            # build the left subtree
            curNode.left = recur(current - right + hashSet[curVal] - 1, left, hashSet[curVal] - 1)
            return curNode
        hashSet = dict()
        n = len(postorder)
        for i in range(n):
            hashSet[inorder[i]] = i
        return recur(n - 1, 0, n - 1)