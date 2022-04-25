'''
0284 Peeking Itertor
'''
'''
A solution that fails to understand it.
'''
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.storage = []
        while iterator.hasNext():
            self.storage.append(iterator.next())
        self.cursor = -1        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.storage[self.cursor + 1]
        

    def next(self):
        """
        :rtype: int
        """
        self.cursor += 1
        return self.storage[self.cursor]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cursor + 1 < len(self.storage)