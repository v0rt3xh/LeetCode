'''
0297 Serialize and Deserialize Binary Tree
# TODO: Update a cpp solution in the future.
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        Serialize the tree in the form of '1,2,3,#,#,4,5,#,#,#,#'
        '#': None
        """
        if not root:
            return ''
        queue = collections.deque()
        queue.append(root)
        res = [str(root.val)]
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                res.append(str(node.left.val))
            else:
                res.append('#')
            if node.right:
                queue.append(node.right)
                res.append(str(node.right.val))
            else:
                res.append('#')
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        # similar BFS deserialize approach
        """
        if data == '':
            return 
        data_list = data.split(',')
        root = TreeNode(int(data_list[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if data_list[i] != '#':
                node.left = TreeNode(int(data_list[i]))
                queue.append(node.left)
            if data_list[i + 1] != '#':
                node.right = TreeNode(int(data_list[i + 1]))
                queue.append(node.right)
            i += 2
        return root