'''
0108 Convert Sorted Array to Binary Search Tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # always choose median? I assume yes
        n = len(nums)
        # Nothing to do
        # return None
        if n == 0:
            return None
        # select median
        mid = n // 2
        # create root by median
        # recursively build the rest
        # maybe the syntax can get improved
        # using array syntax would be slow
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node