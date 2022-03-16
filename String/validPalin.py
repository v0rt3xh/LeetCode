'''
0125 Valid Palindrome
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s) - 1
        # yeah, I used string library.
        lib = string.ascii_letters + string.digits
        while left <= right:
            while left < len(s) and s[left] not in lib:
                left += 1
            while right > -1 and s[right] not in lib:
                right -= 1
            if left > right:
                break
            if s[right] != s[left]:
                return False
            left += 1
            right -= 1
        return True