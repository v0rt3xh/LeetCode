'''
0013 Roman to integer
Hashset
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        # Classic hashset xddd
        hashset = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
             'I': 1
        }
        n = len(s)
        res = 0
        # cursor
        i = 0
        while i < n:
            # next element possible
            if i + 1 < n and s[i: i + 2] in hashset:
                res += hashset[s[i: i + 2]]
                i += 2
                continue
            # should be an else lmao!
            if s[i] in hashset:
                res += hashset[s[i]]
                i += 1
                
        return res