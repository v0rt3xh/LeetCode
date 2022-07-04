'''
0437 Path Sum III
1. DFS
2. Prefix Sum
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Starting from node (choose it),
        # The numbers of path that can add up to targetSum
        def rootSum(node, targetSum):
            if not node:
                return 0
            result = 0
            if node.val == targetSum:
                # Special case, 
                result += 1
            # Add up children's result
            result += rootSum(node.left, targetSum - node.val)
            result += rootSum(node.right, targetSum - node.val)
            return result
        
        if not root:
            return 0
        # Starting from root
        answer = rootSum(root, targetSum)
        # Starting from root's children
        answer += self.pathSum(root.left, targetSum)
        answer += self.pathSum(root.right, targetSum)
        return answer