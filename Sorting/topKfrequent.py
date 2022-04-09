'''
April Challenge
0347 Top K Frequent Elements
Heap week huh?
'''
import heapq # Use library O_o
# define a custom class for comparison
class freqNode:
    def __init__(self, num, freq):
        self.num = num
        self.freq = freq
    def __lt__(self, node):
        return self.freq < node.freq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = dict()
        # First iterate through the array, obtain frequency.
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num] += 1
        # Build a heap (Though using library.)
        # only store k most frequent items
        kHeap = []
        for num in freqMap:
            if len(kHeap) < k:
                heapq.heappush(kHeap, freqNode(num, freqMap[num]))
            else:
                # when length == k, do something
                curVal = kHeap[0].freq
                # larger than current top element, 
                # pop the top element in the heap
                # push current element
                if curVal < freqMap[num]:
                    heapq.heappop(kHeap)
                    heapq.heappush(kHeap, freqNode(num,freqMap[num]))
        # return the require elements.
        return [x.num for x in kHeap]