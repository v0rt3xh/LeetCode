'''
0049 Group Anagrams
'''

# A bit ... how to explain, weird though.
# My solution: Math?

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for s in strs:
            tmpSum = 0
            for c in s:
                tmpSum += 10 ** (ord(c) - ord('a'))
            if tmpSum not in hashMap:
                hashMap[tmpSum] = [s]
            else:
                hashMap[tmpSum].append(s)
        res = []
        for key in hashMap:
            res.append(hashMap[key])
        return res

# Multiply by prime numbers could be okay