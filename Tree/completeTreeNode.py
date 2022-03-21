'''
0222 Count Complete Tree Nodes
Straight Forward: BFS, count / DFS count
'''
'''
Less than O(n)? 
We observe that the height of tree matters.
For a node
if node.left's height == node.right's height,
the left subtree must be complete
if node.left's height > node.right's height
the right subtree must be complete.
(Though on leetcode, the straight forward approach 
seems to be more efficient on those test cases.)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Get the height
    def height(self, root:TreeNode):
        height = 0
        while root:
            root = root.left
            height += 1

        return height

    def countNodes(self, root: TreeNode) -> int:
        # empty just None
        if root == None:
            return 0
        # get the left, right subtree's height
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        
        # height left == height right
        if leftHeight == rightHeight:
            # need to count root.right's num, compute left by height
            return (2 ** leftHeight - 1) + self.countNodes(root.right) + 1
        # height left > height right
        # count root.left's num, compute right by height
        else:
            return (2 ** rightHeight - 1) + self.countNodes(root.left) + 1
'''
Credit
作者：rocky0429-2
链接：https://leetcode-cn.com/problems/count-complete-tree-nodes/solution/acm-xuan-shou-tu-jie-leetcode-by-rocky04-5epi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
