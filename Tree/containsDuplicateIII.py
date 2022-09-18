'''
0220 Contains Duplicate III
Red-Black Tree
'''
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            # Notice that we have fixed size window
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])
            window.add(nums[i])
            loc = bisect.bisect_left(window, nums[i])
            # Get the possible location of numbers that are closest to nums[i]
            if loc > 0 and abs(window[loc] - window[loc - 1]) <= valueDiff:
                return True
            if loc < len(window) - 1 and abs(window[loc + 1] - window[loc]) <= valueDiff:
                return True
        return False