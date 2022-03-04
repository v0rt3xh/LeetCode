'''
0076 Minimum Window Substring
Sliding Window:
    1. two pointers, left and right
    2. three operations
        try to expand right to incorporate all the stuff,
        try to squeeze left to minimize the size of the window,
        advanced left to start new search.
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window
        # Find each 'starting position' of t
        needElement = collections.defaultdict(int)
        # The count of each element in the target string
        for c in t:
            needElement[c] += 1
        # A variable that helps us determine if the string is covered
        remainingAmount = len(t)
        # init left, right boundary for the result 
        res = [0, float('inf')]
        left = 0 # left pointer
        # c: character, j: index, serve as the right pointer
        for j, c in enumerate(s):
            # first step, we increase the size of current window
            # "incorporate more elements"
            if needElement[c] > 0:
                # The element we meet, is an element in t
                # reduce the number of 'remaining amount'
                remainingAmount -= 1
            needElement[c] -= 1
            # second step, squeeze the current window 
            if remainingAmount == 0:
                while True:
                    character = s[left]
                    if needElement[character] == 0:
                        # Cannot continue squeezing, met an essential
                        break
                    needElement[character] += 1
                    left += 1
                # squeeze process ended.
                # compare length of substring
                if j - left < res[1] - res[0]:
                    res[0], res[1] = left, j
                # move the left pointer forward, back to previous steps
                remainingAmount += 1
                needElement[s[left]] += 1
                left += 1
        # Okay, return the result
        if res[1] > len(s): # no update to the indices, return ""
            return ""
        else:
            return s[res[0]: res[1] + 1]
        
        return res