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

'''
Official Solution
Leetcode-Solution @ Leetcode-cn
'''
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next()
        self._hasNext = iterator.hasNext()

    def peek(self):
        return self._next

    def next(self):
        ret = self._next
        self._hasNext = self.iterator.hasNext()
        self._next = self.iterator.next() if self._hasNext else 0
        return ret

    def hasNext(self):
        return self._hasNext
