'''
0395 Longest Substring with 
     At Least K Repeating Characters 

Use this problem as an example for understanding recursion
We only care about inputs and outputs, not the procedure
Stopping condition:
    len(s) < k:
        return 0
Recursive step,
if an element's frequency < k:
split the string according to that element,
recursive steps on the resulting strings. 
'''
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0 # Base case
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        # Every character appears more than k times
        # return the length
        return len(s)