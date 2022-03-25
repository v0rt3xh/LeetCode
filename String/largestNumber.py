'''
0179 Largest Number
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        '''
        We need find a correct ordering.
        normally, x > y just x's value > y's value.
        
        In this case, 
        x >= y means: 'xy' >= 'yx'
        e.g 2 >= 10: '210' >= '102'
        Sort the list in a descending order,
        join the numbers,
        we have the largest number.
        (Actually, here we flip the definition of >=,
        just being lazy XD)
        
        We can choose use sort function with lamda
        Or define a custom merge sort
        '''
        def mergeSort(A):
            n = len(A)
            if n == 1:
                return A
            mid = n // 2
            A1 = mergeSort(A[:mid])
            A2 = mergeSort(A[mid:])
            merged = merge(A1, A2)
            return merged
            
        def merge(list1, list2):
            n, m = len(list1), len(list2)
            res = list()
            cur1, cur2 = 0, 0
            while cur1 < n and cur2 < m:
                str1 = str(list1[cur1])
                str2 = str(list2[cur2])
                if int(str1 + str2) >= int(str2 + str1):
                    res.append(list1[cur1])
                    cur1 += 1
                else:
                    res.append(list2[cur2])
                    cur2 += 1
            while cur1 < n: 
                res.append(list1[cur1])
                cur1 += 1
            while cur2 < m: 
                res.append(list2[cur2])
                cur2 += 1
            return res
        result_list = mergeSort(nums)
        result = ''
        for res in result_list:
            result += str(res)
        # A special case ... 
        if result[0] == '0':
            return '0'
        return result

'''
Sorted function:
Credit: maomao @ leetcode-CN
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y): return int(y+x) - int(x+y)
        nums = sorted(map(str, nums), key=cmp_to_key(compare))
        return "0" if nums[0]=="0" else "".join(nums)