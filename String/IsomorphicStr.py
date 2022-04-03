'''
0205 Isomorphic String
'''
'''
Basic version, should be improved
We use two hash maps to store the mapping
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sSet = dict()
        tSet = dict()
        # An important aspect: Must not assigned to the same character
        for cs, ct in zip(s, t):
            if cs not in sSet and ct not in tSet:
                sSet[cs] = ct
                tSet[ct] = cs
            else:
                if cs in sSet and sSet[cs] != ct:
                    return False
                if ct in tSet and tSet[ct] != cs:
                    return False
        return True
'''
Credit: @StrayCamel
Maybe we can use this information:
Number of unique character in s == ~ in t
There are only len(s) / len(t) 's (cs, ct) mapping
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) and len(set(s)) == len(set(zip(s, t)))