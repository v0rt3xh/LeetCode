'''
0009 Palindrome Number
.... can I say I only know the str transform??
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        cheat = str(x)
        left = 0
        right = len(cheat) - 1
        while left <= right:
            if cheat[left] == cheat[right]:
                left += 1
                right -= 1
                continue
            return False
        return True
'''
... Math approach, my way is not that smart though.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        stack = []
        while x:
            stack.append(x % 10)
            x //= 10
        res = 0
        base = 1
        while stack:
            res += base * stack.pop()
            base *= 10
        return res == tmp

'''
without explicit stack!!
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        return res == tmp
        