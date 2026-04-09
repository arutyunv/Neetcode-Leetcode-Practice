### Two Stacks solution ### 

class MinStack:

    def __init__(self):
        # Maintain two stacks: 
        # Stack 1. self.stack stores all pushed values 
        self.stack = []
        # Stack 2. minStack stores the minim so far at each levl 
        self.minStack = []

    def push(self, val: int) -> None:
        # Push to original stack (simple)
        self.stack.append(val)

        # Push to minStack: compute new minum between val and current minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        # push this minimum to minStack
        self.minStack.append(val)
        

    def pop(self) -> None:
        # Pop from initial stack
        self.stack.pop()

        # Pop from minStack to keep two stacks aligned
        self.minStack.pop()

    def top(self) -> int:
        # Return the top of stack
        return self.stack[-1]
        

    def getMin(self) -> int:
        # Return the top of minStack, which is the current minimum
       return self.minStack[-1] 
