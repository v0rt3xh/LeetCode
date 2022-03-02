'''
    003 Longest Substring without repeating characters.
    Find the length of the ~
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Sliding window. We use two pointers. 
        # Left pointer starts at the left end, 
        # We try to move the right pointer as far as possible.
        # When we met a repeated character 
        # Record current length & compare with the maximum one
        # Move the left pointer to the right 
        # Until there is no repeated element.
        # Expand right again.
        # Notice some boundary cases.
        n = len(s)
        if n == 0: # Special case
            return 0
        maxLen = 0
        lookup = set() # A hash set to store observations.
        right = -1 # Trick, place right at -1
        for i in range(n): # The loop is the left pointer
            if i != 0: # Corner case
                # Remove the character
                lookup.remove(s[i - 1])
            # move the right pointer
            while right < n - 1 and s[right + 1] not in lookup:
                lookup.add(s[right + 1])
                right += 1
            # Now from left to right, right - i + 1 is the current max length
            maxLen = max(maxLen, right - i + 1)
        return maxLen


