'''
0101 SymmetricTree
BFS and DFS
BFS approach is rather straight forward.
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # BFS queue, should have named as queue though 
        stack = [root.left, root.right]
        while stack:
            # current number of children nodes
            n = len(stack)
            # first iteration, justify symmetric properties
            for i in range(n//2):
                # None case
                if (not stack[i]) and stack[n - 1 - i]:
                    return False
                if (not stack[n - 1 - i]) and stack[i]:
                    return False
                # compare value case
                if stack[i] and stack[n - 1 - i]:
                    if stack[i].val != stack[n - 1 - i].val:
                        return False
            # second iteratio to update the queue
            for j in range(n):
                node = stack.pop(0)
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
        return True

'''
DFS approach, tricky??
nah, we need a recursive helper with 2 syntax
'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # left & right Nodes
        def recur(leftNode, rightNode):
            # Both empty, just return True
            if not leftNode and not rightNode:
                return True
            # Not empty, compare value
            if rightNode and leftNode:
                # only when the symmetric property is satisfied,
                # start the recursive process
                if rightNode.val == leftNode.val:
                    # Notice how we start the following work
                    return recur(leftNode.left, rightNode.right) and recur(leftNode.right, rightNode.left)
            # other situations, just False
            return False
        # return that value bruh
        return recur(root.left, root.right)
                    