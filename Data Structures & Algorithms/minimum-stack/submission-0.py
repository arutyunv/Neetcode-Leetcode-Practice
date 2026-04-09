### BRUTE FORCE ##

class MinStack:

    def __init__(self):
        # Just a normal Python list acting as a stack 
        self.stack = []

    def push(self, val: int) -> None:
        # Add an element to the top 
        self.stack.append(val)

    def pop(self) -> None:
        # Remove the top element from the stack
        self.stack.pop()

    def top(self) -> int:
        # Read out the top element 
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Step 1. Create an empty temp stack 
        tmp = []
        
        # Step 2. Empty the stack completely while tracking the min of the original stack to find min
        mini = self.stack[-1]
        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        # Step 3. Rebuilds the original stack
        while len(tmp):
            self.stack.append(tmp.pop())

        return mini
        
