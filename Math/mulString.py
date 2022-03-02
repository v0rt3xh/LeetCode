'''
0043 Multiply Strings
# a basic solution - Credit: Leetcode-CN
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        ans = "0"
        m, n = len(num1), len(num2)
        for i in range(n - 1, -1, -1):
            add = 0
            y = int(num2[i])
            # why? this is how you do the multiplication
`           # 123 * 456
                    #     7 3 8`
                    #   6 1 5 0
                    # 4 9 2 0 0   
            curr = ["0"] * (n - i - 1)
            for j in range(m - 1, -1, -1):
                product = int(num1[j]) * y + add
                curr.append(str(product % 10))
                add = product // 10
            if add > 0:
                curr.append(str(add))
            curr = "".join(curr[::-1])
            # Add current result to the answer string 
            ans = self.addStrings(ans, curr)
        
        return ans
    
    def addStrings(self, num1: str, num2: str) -> str:
        # This comes from previous problem: adding strings
        i, j = len(num1) - 1, len(num2) - 1
        add = 0
        ans = list()
        # notice the iterative condition:
        # either - i / j ends or we have carry over!
        while i >= 0 or j >= 0 or add != 0:
            # out of bound then 0 ...
            # Thus, we don't have to append 0 at the beginning 
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            result = x + y + add
            # append current result, we will flip the string at the end 
            ans.append(str(result % 10))
            # carry over
            add = result // 10
            i -= 1
            j -= 1
        # flip the result
        return "".join(ans[::-1])

'''
Improving the performance by introducing array
nums1 len: n
nums2 len: m
the maximum length of their multiplication result:
    n * m 
    (10^n - 1) (10^m - 1)
use an array with length n + m to store the result
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        ansArr = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            for j in range(n - 1, -1, -1):
                ansArr[i + j + 1] += x * int(num2[j])
        
        for i in range(m + n - 1, 0, -1):
            ansArr[i - 1] += ansArr[i] // 10
            ansArr[i] %= 10
        
        index = 1 if ansArr[0] == 0 else 0
        ans = "".join(str(x) for x in ansArr[index:])
        return ans

    #作者：LeetCode-Solution
    #链接：https://leetcode-cn.com/problems/multiply-strings/solution/zi-fu-chuan-xiang-cheng-by-leetcode-solution/  
    #来源：力扣（LeetCode）
    #著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    