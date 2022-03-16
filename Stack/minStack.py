'''
0155 Min Stack
'''
class MinStack:

    def __init__(self):
        '''
        A for ordinary stack
        B for min elements
        '''
        self.A = []
        self.B = []
        
    def push(self, val: int) -> None:
        self.A.append(val)
        '''
        Empty min element stack, just append
        O.W. compared to current min
        '''
        if not self.B:
            self.B.append(val)
        else:
            if val <= self.B[-1]:
                self.B.append(val)

    def pop(self) -> None:
        # pop when something exists
        if self.A:
            val = self.A.pop()
            # check the value and operate on B
            if self.B and self.B[-1] == val:
                self.B.pop()

    def top(self) -> int:
        return self.A[-1]
        

    def getMin(self) -> int:
        return self.B[-1]