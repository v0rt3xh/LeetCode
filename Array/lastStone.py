'''
1046 Last Stone Weight
'''
'''
Using library's heap
Should review heap's implementation though!
'''
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                newStone = stone1 - stone2
                heapq.heappush(stones, newStone)
        if stones:
            return -stones[0]
        return 0