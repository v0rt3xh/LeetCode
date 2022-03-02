'''
0094 Binary Tree Inorder Traversal
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive Approach
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [] # At the start, nothing to return
        if not root: # If the node is empty, just skip it
            return res
        # Left child first
        res += self.inorderTraversal(root.left)
        # Then process the value
        res.append(root.val)
        # Right child last
        res += self.inorderTraversal(root.right)
        return res
        # Also possible by defining a helper function / method
    

# Harder option: How would you write an iterative approach?

'''
Simulating the recursive process!
root -> push to call stack -> root = root.left
if current 'root' is empty, stop, and pop a node from the stack
append the value of the node; add the node's right to the stack.
Until either not root not stack

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        callStack = []
        while callStack or root:
            if root:
                callStack.append(root)
                root = root.left
            else:
                tmp = callStack.pop()
                res.append(tmp.val)
                root = tmp.right
        return res

'''