'''
0235 Lowest Common Ancestor of a Binary Search Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Not sure this lower, higher step necessary or not.
        Actually don't have to
        just root.val < lower & higher (i.e, p and q)
        or root.val > lower & higher
        Don't have to add the min max!
        '''
        lower, higher = min(p.val, q.val), max(p.val, q.val)
        if lower <= root.val and root.val <= higher:
            return root
        elif root.val < lower:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > higher:
            return self.lowestCommonAncestor(root.left, p, q)

'''
Itertative Step
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while True:
            if cur.val < p.val and cur.val < q.val:
                cur = cur.right
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                return cur