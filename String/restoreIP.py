'''
0093 Restore IP Addresses
backtracking of course
but how?
I think I need more practice for backtracking

Credit: 
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/restore-ip-addresses/solution/fu-yuan-ipdi-zhi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        SEG_COUNT = 4
        ans = list()
        segments = [0] * SEG_COUNT
        # segId: the i-th segment of the IP address 0, 1, 2, 3
        # segStart: the starting position in the string.
        def dfs(segId: int, segStart: int):
            # If you have found 4 segments, ready to return
            if segId == SEG_COUNT:
                # only when we complete the string
                if segStart == len(s):
                    ipAddr = ".".join(str(seg) for seg in segments)
                    ans.append(ipAddr)
                return
            
            # we did not find all the segments, terminate the process
            if segStart == len(s):
                return
            # dealing with leading 0
            if s[segStart] == "0":
                segments[segId] = 0
                dfs(segId + 1, segStart + 1)
            
            # Ordinary steps
            addr = 0
            for segEnd in range(segStart, len(s)):
                # compute the current number
                addr = addr * 10 + (ord(s[segEnd]) - ord("0"))
                # if within (0, 255)
                # start recursive step
                # o.w. terminate the loop
                if 0 < addr <= 0xFF:
                    segments[segId] = addr
                    dfs(segId + 1, segEnd + 1)
                else:
                    break
        

        dfs(0, 0)
        return ans

