'''
0225 Implement Stack Using Queues
'''
class MyStack:

    def __init__(self):
        # default double-ended queue in Python
        self.A = collections.deque([])
        

    def push(self, x: int) -> None:
        # append the element
        self.A.append(x)

    def pop(self) -> int:
        # Here, we use the iterative method
        # So, why don't you finish it in the push step ...???
        size = len(self.A)
        i = size - 1
        while i:
            value = self.A.popleft()
            self.A.append(value)
            i -= 1
        return self.A.popleft()

    def top(self) -> int:
        size = len(self.A)
        i = size # top not pop
        while i:
            value = self.A.popleft()
            self.A.append(value)
            i -= 1
        return value

    def empty(self) -> bool:
        return len(self.A) == 0

'''
Improved Version
'''
class MyStack:

    def __init__(self):
        self.A = collections.deque([])
        

    def push(self, x: int) -> None:
        size = len(self.A)
        self.A.append(x)
        for _ in range(size):
            self.A.append(self.A.popleft())

    def pop(self) -> int:
        return self.A.popleft()

    def top(self) -> int:
        return self.A[0]

    def empty(self) -> bool:
        return len(self.A) == 0
        