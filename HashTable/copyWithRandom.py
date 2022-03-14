'''
0138 Copy List with Random Pointer
Used a hash table.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        sentinel = Node(0)
        cursor = head
        editor = sentinel
        helperHash = dict()
        # special case
        helperHash[None] = None
        # create new node and the mapping
        while cursor:
            newNode = Node(cursor.val)
            helperHash[cursor] = newNode
            cursor = cursor.next
        cursor = head
        # catenate next / random
        while cursor:
            helperHash[cursor].next = helperHash[cursor.next]
            helperHash[cursor].random = helperHash[cursor.random]
            editor.next = helperHash[cursor]
            cursor = cursor.next
            editor = editor.next
        return sentinel.next