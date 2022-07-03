'''
0394 Decode String
Stack for numbers 
Stack for strings
'''
# My solution, a bit clumsy
class Solution1:
    def decodeString(self, s: str) -> str:
        num_stack = list()
        string_stack = list()
        running_num = ''
        result = ''
        for c in s:
            if '0' <= c <= '9':
                running_num += c
            elif c == '[':
                num_stack.append(int(running_num))
                running_num = ''
                string_stack.append(c)
            elif c == ']':
                characters = ''
                while True:
                    element = string_stack.pop()
                    if element == '[':
                        break
                    characters = element + characters
                repeated_times = num_stack.pop()
                string_stack.append(characters * repeated_times)
            else:
                result += c
        for c in string_stack:
            result += c
        return result

# Concise Solution, from Krahets (jyd) @ Leetcode CN; 
class Solution2:
    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == '[':
                stack.append([multi, res])
                res, multi = "", 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= c <= '9':
                multi = multi * 10 + int(c)            
            else:
                res += c
        return res
