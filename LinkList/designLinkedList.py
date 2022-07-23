'''
0707 Design Linked List
Double ended 
'''
class Node:
    def __init__(self, value=0):
        self.val = value
        self.next, self.prev = None, None
    

class MyLinkedList:

    def __init__(self):
        self.sentinel_head, self.sentinel_tail = Node(0), Node(0)
        self.size = 0
        # Sentinel head and sentinel tail
        self.sentinel_head.next = self.sentinel_tail
        self.sentinel_tail.prev = self.sentinel_head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        # Decide traverse from head or tail
        if self.size - index > index + 1:
            # Start from head
            cursor = self.sentinel_head
            for _ in range(index + 1):
                cursor = cursor.next
        else:
            cursor = self.sentinel_tail
            for _ in range(self.size - index):
                cursor = cursor.prev
        return cursor.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        self.size += 1
        newNode.next = self.sentinel_head.next
        newNode.prev = self.sentinel_head
        self.sentinel_head.next.prev = newNode
        self.sentinel_head.next = newNode


    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        self.size += 1
        newNode.next = self.sentinel_tail
        newNode.prev = self.sentinel_tail.prev
        self.sentinel_tail.prev.next = newNode
        self.sentinel_tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        # Sanity check
        if index > self.size:
            return
        
        # [Weird case], negative index treat as 0
        if index < 0:
            index = 0
        
        # Decide traverse order
        if index < self.size - index:
            prevNode = self.sentinel_head
            for _ in range(index):
                prevNode = prevNode.next
            nextNode = prevNode.next
        else:
            nextNode = self.sentinel_tail
            for _ in range(self.size - index):
                nextNode = nextNode.prev
            prevNode = nextNode.prev
        
        # Add 
        newNode = Node(val)
        self.size += 1
        prevNode.next = newNode
        newNode.next = nextNode
        nextNode.prev = newNode
        newNode.prev = prevNode
        
    def deleteAtIndex(self, index: int) -> None:
        # Sanity check
        if index < 0 or index >= self.size:
            return 
        # Decide traverse order
        if index < self.size - index:
            prevNode = self.sentinel_head
            for _ in range(index):
                prevNode = prevNode.next
            nextNode = prevNode.next.next
        else:
            nextNode = self.sentinel_tail
            for _ in range(self.size - index - 1):
                nextNode = nextNode.prev
            prevNode = nextNode.prev.prev
        
        self.size -= 1
        prevNode.next = nextNode
        nextNode.prev = prevNode

