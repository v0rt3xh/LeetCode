'''
0622 Design Circular Queue
I think my double ended linked list does not satisfy the constraint?
'''
class Node:
    def __init__(self, val=0, nex=None, prev=None):
        self.val = val
        self.next = nex
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = Node(value)
        self.sentinel.prev.next = newNode
        newNode.prev = self.sentinel.prev
        newNode.next = self.sentinel
        self.sentinel.prev = newNode
        self.size += 1
        return True
            

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        deleteNode = self.sentinel.next
        deleteNode.next.prev = self.sentinel
        self.sentinel.next = deleteNode.next
        deleteNode.next = None
        deleteNode.prev = None
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.sentinel.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.sentinel.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Official Solution:
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0]*k
        self.headIndex = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        self.queue[(self.headIndex + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # empty queue
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """

        return self.count == self.capacity
'''
Credit: LeetCode Solution
'''