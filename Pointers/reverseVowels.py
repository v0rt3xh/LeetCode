'''
0345 Reverse Vowels of A String
Double pointers,
when left, right point to Vowels, swap them.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowels(character):
            return character in 'aeiouAEIOU'
        # Cannot directly swap within a string in Python
        s = list(s)
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            # Do not want out of range < n / > 0
            while left < n and not isVowels(s[left]):
                left += 1
            while right > 0 and not isVowels(s[right]):
                right -= 1
            if left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return ''.join(s)