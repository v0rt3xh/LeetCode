'''
0105
Construct Binary Tree from Preorder and Inorder Traversal
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # We first need to hashset to store positions in inorder
        def recur(cur, left, right):
            '''
            current: current position 'root' in preorder
            left: boundary of its left subtree (inOrder's)
            right: right boundary of its rightsubtree (inOrder's)
            '''
            # left index greater than right, return Null
            if left > right:
                return None
            # get current value in preorder
            curVal = preorder[cur]
            node = TreeNode(curVal)
            # create current node
            # recursive step for the left subtree
            # update cur: root's index: just cur + 1
            # update left: For the left subtree, it's still left
            # update right: For the right subtree, 
            #               curVal 's position in inorder - 1
            node.left = recur(cur + 1 , left, hashSet[curVal] - 1)
            # recursive step for the right subtree
            # update cur: root's index: cur + len(leftCandidates) + 1
                                        # len(leftCandidates) = hashSet[curVal] - left
            # update left: For the right subtree,  hashSet[curVal] + 1
            # update right: For the right subtree, 
            #               still right
            node.right = recur(cur + hashSet[curVal] - left + 1, hashSet[curVal] + 1, right)
            return node
        hashSet = dict()
        n = len(preorder)
        for i in range(n):
            hashSet[inorder[i]] = i
        res = recur(0, 0, n - 1)
        return res