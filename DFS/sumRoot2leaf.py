'''
0129 Sum Root to Leaf Numbers
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
My method, not that elegent
'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        # node is not None in this problem
        def recur(node, preSum):
            # compute the value first
            preSum = 10 * preSum + node.val
            # leaf -> add to overall sum
            if not node.left and not node.right:
                self.res += preSum
                return
            # left is not None, start recursive step
            if node.left:
                recur(node.left, preSum)
            if node.right:
                recur(node.right, preSum)
        recur(root, 0)
        return self.res
        
'''
Pro's way
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, prevTotal: int) -> int:
            if not root:
                return 0
            total = prevTotal * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return dfs(root.left, total) + dfs(root.right, total)

        return dfs(root, 0)
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/solution/qiu-gen-dao-xie-zi-jie-dian-shu-zi-zhi-he-by-leetc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''