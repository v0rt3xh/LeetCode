'''
0187 Repeated DNA Sequences
A straight forward way
Look for all the subsequences with length 10
Hash counter, wow
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        hashSet = defaultdict(int)
        for i in range(len(s) - 10 + 1):
            curSeq = s[i: i + 10]
            hashSet[curSeq] += 1
            if hashSet[curSeq] == 2:
                # count == 2, append
                res.append(curSeq)
        return res