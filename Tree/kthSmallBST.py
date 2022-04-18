'''
0230 Kth Smallest Element in a BST
'''
'''
Naive approach
'''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in-order
        def recur(node):
            if not node:
                return 
            recur(node.left)
            storage.append(node.val)
            recur(node.right)
        
        storage = []
        recur(root)
        return storage[k - 1]
'''
A slight improvement:
    get the number of nodes of each subtree.
For instance:
    root - to its left: m nodes, m < k
    then, the k-th smallest must in root.left / root
'''
class MyBst:
    def __init__(self, root: TreeNode):
        self.root = root

        # node_num, the number of nodes in the subtree of a give 'root'
        self._node_num = {}
        self._count_node_num(root)

    def kth_smallest(self, k: int):
        """Get the k-th smallest item"""
        node = self.root
        while node:
            left = self._get_node_num(node.left)
            if left < k - 1:
                node = node.right
                k -= left + 1
            elif left == k - 1:
                return node.val
            else:
                node = node.left

    def _count_node_num(self, node) -> int:
        """starting from node, the number nodes in its subtree"""
        if not node:
            return 0
        self._node_num[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node_num[node]

    def _get_node_num(self, node) -> int:
        """Get the number of nodes in subtree rooted at node"""
        return self._node_num[node] if node is not None else 0


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        bst = MyBst(root)
        return bst.kth_smallest(k)
'''
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/solution/er-cha-sou-suo-shu-zhong-di-kxiao-de-yua-8o07/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

'''
Follow-up: What if we frequently add & delete element?
Self-balancing BST
A bit complicated though.
'''