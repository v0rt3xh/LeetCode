'''
0703 Kth Largest Element in a Stream
Classic heap
'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_k = [] # Store the top k largest item
        self._k = k
        for num in nums: # init
            heapq.heappush(self.heap_k, num)

    def add(self, val: int) -> int:
        # push the val into the heap
        heapq.heappush(self.heap_k, val)
        # If length larger than k
        # throw out those smaller items
        while len(self.heap_k) > self._k:
            heapq.heappop(self.heap_k)
        return self.heap_k[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

