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

'''
2. Prefix Sum
'''
class Solution2:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # prefix sum:
        # The sum of node values, starting from the root 
        # and right before current node
        # Thus, if current sum is 18, target is 8, 
        # Then margin is 10, we want to know if 10 is in the prefix list
        # if yes, just add up its corresponding frequency
        prefixSum = collections.defaultdict(int)
        prefixSum[0] = 1
        
        def dfs(node, current_sum):
            if not node:
                return 0
            result = 0
            # Update current prefix sum
            current_sum += node.val
            # Get the margin, check if it has presented.
            result += prefixSum[current_sum - targetSum]
            # For the following recursion
            # update prefix sum dictionary
            prefixSum[current_sum] += 1
            # recursive steps
            result += dfs(node.left, current_sum)
            result += dfs(node.right, current_sum)
            # remember to remove current input
            prefixSum[current_sum] -= 1
            return result 
        
        return dfs(root, 0)