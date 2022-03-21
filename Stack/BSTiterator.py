'''
0173 Binary Search Tree Iterator
Behind the scene: 
    How would you simulate the inorder recursive process
    with a stack.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        '''
        Use a stack as a processing unit
        '''
        self.stack = []
        while root:
            '''
            Store the left nodes
            '''
            self.stack.append(root)
            root = root.left

    def next(self):
        # Current value is 'next'
        cur = self.stack.pop()
        node = cur.right
        # We also need to append more left nodes
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self):
        '''
        Something in the stack, then hasNext is True
        '''
        return len(self.stack) > 0
'''
作者：fuxuemingzhu
链接：https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/fu-xue-ming-zhu-dan-diao-zhan-die-dai-la-dkrm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''