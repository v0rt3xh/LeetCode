'''
0897 Increasing Order Search Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    '''
    A straight-forward method.
    But not that efficient.
    '''
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recur(node):
            if not node:
                return
            recur(node.left)
            queue.append(node)
            recur(node.right)
        queue = deque()
        recur(root)
        head = TreeNode()
        prev = head
        while queue:
            node = queue.popleft()
            node.left = None
            node.right = None
            prev.right = node
            prev = node
        return head.right

'''
A different approach
Recursive, but change left / right while doing the recursion
'''
class Solution(object):
    def increasingBST(self, root):
        dummy = TreeNode(-1)
        self.prev = dummy
        self.inOrder(root)
        return dummy.right
        
    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        root.left = None
        self.prev.right = root
        self.prev = root
        self.inOrder(root.right)

'''
作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/increasing-order-search-tree/solution/fu-xue-ming-zhu-fen-xiang-er-cha-shu-san-hljt/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''            
        

