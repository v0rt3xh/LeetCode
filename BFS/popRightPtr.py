'''
0116 Populating Next Right Pointers in Each Node

'''
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        queue = [root]
        while queue:
            tmpNode = None
            for i in range(len(queue)):
                curNode = queue.pop(0)
                if curNode.left and curNode.right:
                    queue.append(curNode.left)
                    queue.append(curNode.right)
                if tmpNode:
                    tmpNode.next = curNode
                tmpNode = curNode
        return root

# Follow-up:
# O(1) Space

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 从根节点开始
        leftmost = root
        
        while leftmost.left:
            
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # 指针向后移动
                head = head.next
            
            # 去下一层的最左的节点
            leftmost = leftmost.left
        
        return root 