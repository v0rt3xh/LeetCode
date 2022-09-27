'''
0306 Additive Number
Credit: Leetcode Solution
https://leetcode.cn/problems/additive-number/solution/lei-jia-shu-by-leetcode-solution-cadc/
'''

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        num_of_element = len(num)
        # We enumerate the possible starting position of the second elements. 
        for secondStart in range(1, num_of_element - 1):# Left a place for thirds
            if num[0] == '0' and secondStart != 1:
                break # No leading zeros for the first element
            for secondEnd in range(secondStart, num_of_element - 1):
                if num[secondStart] == '0' and secondEnd != secondStart:
                    break # No leading zeros for the second element
                if self.valid(secondStart, secondEnd, num):
                    # Recursively check other possible location
                    # Once satisfied, just return 
                    return True
        return False
        
    def valid(self, secondStart: int, secondEnd: int, num: str) -> bool:
        num_of_element = len(num)
        firstStart, firstEnd = 0, secondStart - 1
        while secondEnd < num_of_element:
            third = self.stringAdd(num, firstStart, firstEnd, secondStart, secondEnd)
            thirdStart = secondEnd + 1
            thirdEnd = secondEnd + len(third)
            if thirdEnd >= num_of_element or num[thirdStart: thirdEnd + 1] != third:
                break # No possible third, just break
            if thirdEnd == num_of_element - 1: # reach the end, okay
                return True
            # Something leftover, continue checking
            firstStart, firstEnd = secondStart, secondEnd
            secondStart, secondEnd = thirdStart, thirdEnd
        return False
    
    def stringAdd(self, s: str, firstStart: int, firstEnd: int, secondStart: int, secondEnd: int) -> str:
        third = []
        carryOver, cur = 0, 0
        while firstEnd >= firstStart or secondEnd >= secondStart or carryOver != 0:
            cur = carryOver
            if firstEnd >= firstStart:
                cur += ord(s[firstEnd]) - ord('0')
                firstEnd -= 1
            if secondEnd >= secondStart:
                cur += ord(s[secondEnd]) - ord('0')
                secondEnd -= 1
            carryOver = cur // 10
            cur %= 10
            third.append(chr(cur + ord('0')))
        return ''.join(third[::-1])
        
        