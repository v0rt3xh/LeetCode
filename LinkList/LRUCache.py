'''
0146 LRU Cache
Hash table and doubly linked list
'''
class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    '''
    Hash Table and Doubly Linked List.
    Data: (key, value) pair,
    1.The node of doubly linked list: (key, value),
      We have a sentinel head and a sentinel tail. 
      Most recently used key is next to head.
    2.As for the hash table, we store (key, node[key] in the linked list)
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        '''
        First check if the key exist, if not, return -1
        The key exist:
            locate the key using hash table.
            Move the corresponding node to the beginning of the linked list
        '''
        if key not in self.cache:
            return -1
        theNode = self.cache[key]
        self.moveToHead(theNode)
        return theNode.value
        

    def put(self, key: int, value: int) -> None:
        '''
        If key not exist,
            create a new node (key value pair) first.
            If size > capacity, remove the last one
        If exist,
            update the value
        '''
        if key not in self.cache:
            newNode = DLinkedNode(key, value)
            self.cache[key] = newNode
            self.addToHead(newNode)
            self.size += 1
            if self.size > self.capacity:
                removeNode = self.removeTail()
                self.cache.pop(removeNode.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
            
    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)
    
    def removeTail(self):
        node = self.tail.prev 
        self.removeNode(node)
        return node
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

'''
Credit:
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''