'''
0095 Unique Binary Search Trees
Your intuition is correct.
Enumerate by root
Left subtree takes [start, i - 1],
right subtree takes [i + 1, end],
Then how to build recursive steps?
At every root, we get possible tree structure by:
adding left possible trees
adding right possible trees
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # recur helper
        # left > right should not happen!
        def buildTree(start, end):
            if start > end:
                return [None]
            # All possible subtrees
            treeCollections = []
            # the possible roots 
            for i in range(start, end + 1):
                # left candidates
                leftOptions = buildTree(start, i - 1)
                # right candidates
                rightOptions = buildTree(i + 1, end)
                # create the tree
                for l in leftOptions:
                    for r in rightOptions:
                        curRoot = TreeNode(i)
                        curRoot.left = l
                        curRoot.right = r
                        treeCollections.append(curRoot)
            return treeCollections
        
        return buildTree(1, n)