'''
0239 Sliding Window Maximum
Monotone Stack
When we meet an element A, 
remove the elements in the queue that are smaller than A 
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ascend_queue = collections.deque()
        # init
        for i in range(k):
            # We keep the larger items that appear later
            while ascend_queue and nums[i] > ascend_queue[-1]:
                ascend_queue.pop()
            ascend_queue.append(nums[i])
        result = [ascend_queue[0]]
        for j in range(k, len(nums)):
            # if the number we are going to pop
            # is the first element in queue, pop from the queue as well
            if nums[j - k] == ascend_queue[0]:
                ascend_queue.popleft()
            # Add new element & remove smaller items
            while ascend_queue and nums[j] > ascend_queue[-1]:
                ascend_queue.pop()
            ascend_queue.append(nums[j])
            result.append(ascend_queue[0])
        return result