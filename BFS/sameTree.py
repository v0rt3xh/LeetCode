'''
0100 SameTree
A simple BFS should suffice.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = [(p, q)]
        # Use a queue to simulate the BFS process
        # Non-empty then proceed.
        while queue:
            p1, p2 = queue.pop(0) # pop out current unit
            # Only consider forward processing cases:
            # case 1, p1 and p2 are non-empty having the same values
            if p1 and p2 and p1.val == p2.val:
                # Append their children
                queue.append((p1.left, p2.left))
                queue.append((p1.right, p2.right))
                continue
            # Both of them are empty
            if not p1 and not p2:
                continue
            # Otherwise, do not proceed
            return False
        # Congrats, you have made it.
        return True

'''
dfs version

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q: return p == q
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
'''
