'''
0114 Flatten Binary Tree into Linked List
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        A straight forward approach.
        Post - order? + right first
        """
        if not root:
            return
        stack = []
        def recur(node):
            if not node:
                return
            recur(node.right)
            recur(node.left)
            stack.append(node)
        recur(root)
        preNode = stack.pop()
        while stack:
            curNode = stack.pop()
            preNode.right = curNode
            preNode.left = None
            preNode = curNode
        return root
'''
O(1) extra space?
We only need previous node
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        
        stack = [root]
        # Preve node by default is None
        prev = None
        
        while stack:
            # current node
            curr = stack.pop()
            if prev: # if previous one exist
            ```````` # Change it to linked list according to the defintion
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            # Only when exist, append into the stack,
            # notice, right first enter the stack.
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。