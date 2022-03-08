'''
0066 Plus One
'''

'''
Solution 1: Not an elegant one, try harder.
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # I assume the insert process would takes a long long time
        # length <= 100, I guess we can traverse at no cost?
        n = len(digits)
        newDigits = [0] * (n + 1)
        newDigits[0] = 1
        i = n - 1
        pre = 1
        while i > -1:
            newDigits[i + 1] = (pre + digits[i]) % 10
            pre = (pre + digits[i]) // 10
            i -= 1
        if pre > 0:
            return newDigits
        else:
            return newDigits[1:]

'''
Solution 2: 
All we have to do, is deal with the damn nine!
'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        i = n - 1
        while i > -1:
            # first element that is not 9
            if digits[i] != 9:
                digits[i] += 1
                for l in range(i + 1, n):
                    digits[l] = 0
                return digits
            i -= 1
        # otherwise, all 9's in digits
        return [1] + [0] * n