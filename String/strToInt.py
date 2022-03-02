'''
0008 string to int (atoi)
????
Automaton!!
Finite State
ALWAYS HAVE: START STATE & END STATE
STATES LIST
    start
    sign
    number
    end
TRANSITION MATRIX
        start   sign    number   end
start   space   +-       0-9     others
sign     NA     NA       0-9     others
number   NA     NA       0-9     others
end  not +- or num NA     NA      ALL


'''
class Solution:
    '''
    Err... extremely chubby
    '''
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        flag = 1
        res = ''
        for i in range(len(s)):
            if i == 0 and s[i] in '+-':
                flag = int(s[i] + '1')
                continue
            if '0' <= s[i] <= '9':
                res += s[i]
            else:
                break
        if res:
            result = flag * int(res)
            if result > 2 ** 31 - 1:
                return 2 ** 31 - 1
            if result < -2 ** 31:
                return - 2 ** 31
            return result
        else:
            return 0

'''
THE ULTIMATE GOD
'''

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        
    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans
