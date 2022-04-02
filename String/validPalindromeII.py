'''
0680 Valid Palindrome II
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # use lambda function to define 'isPalindrome'
        isPalindrome = lambda x: x == x[::-1]        
        left, right = 0, len(s) - 1
        while left <= right:
            # (I'm not sure if it works like a cheat.) 
            if s[left] != s[right]:
                # the key idea is that,
                # sometimes you need to decide which one to delete 
                # (left or right)
                return isPalindrome(s[left:right]) or isPalindrome(s[left + 1: right + 1])
            else:
                left += 1
                right -= 1
        return True