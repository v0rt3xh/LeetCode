'''
0236 Lowest Common Ancestor of a Binary Tree
A classic problem. 
Must-have
Credit: @ Krahets, Leetcode-cn
'''
# Cases: 
# 1:  - node - 
#   p           q

# 2: ... - p -  ... (q in left or right subtree )
#  q          q

# 3: ... - q - ... (p in left or right subtree)
#  p          p


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            # Termination of the recursion
            # reach leaf or find p / q
            return root
        
        # If we haven't find p/q; Start recursive steps!
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # Discuss different cases
        if not left:
            # p & q must in the right subtrees
            # get result from right
            return right
        if not right:
            # similar to previous case
            return left
        if not left and not right:
            # nothing found, return null
            return
        # otherwise, p - root - q ! return root
        return root


