'''
0297 Serialize and Deserialize Binary Tree
Another classic problem,
The key issue is how would you decode it
'''
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        We use '#' to denote Null nodes
        ',' to separate the items
        So, the result would end with: '100,' An extra ','
        """
        queue = collections.deque([])
        queue.append(root)
        self.cache = ''
        while queue:
            node = queue.popleft()
            if node:
                self.cache += str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            else:
                self.cache += '#,'
        return self.cache
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Deal with extra ','
        element_list = data[:-1].split(',')
        root_node = element_list[0]
        if root_node == '#':
            return None
        else:
            root = TreeNode(int(root_node))
        queue = collections.deque([])
        # Important cursor i 
        i = 1
        queue.append(root)
        while queue:
            node = queue.popleft() 
            # Not None, then create the node
            if element_list[i] != '#':
                node.left = TreeNode(int(element_list[i]))
                queue.append(node.left)
            i += 1
            if element_list[i] != '#':
                node.right = TreeNode(int(element_list[i]))
                queue.append(node.right)
            i += 1
        return root