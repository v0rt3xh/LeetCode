'''
0151 Reverse Words in a String
I used built-in functions.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        # Trim
        s = s.strip()
        n = len(s)
        left = 0
        # We can use a deque though.
        # -> no need to reverse at the end
        path = []
        while left < n:
            # move to the next non-space character
            while s[left] == ' ':
                left += 1
            # expand current word
            right = left 
            while s[right] != ' ':
                right += 1
                # reach the end, break
                if right >= n:
                    break
            # append to the list
            path.append(s[left:right])
            left = right
        # formatting output
        res = ' '.join(path[::-1])
        return res