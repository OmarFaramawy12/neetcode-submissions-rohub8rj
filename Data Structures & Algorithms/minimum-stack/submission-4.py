class MinStack:

    def __init__(self):
        # initializes the stack
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        #Insert the item onto stack
        self.stack.append(val)
        # handlin the first case (min stack is empty)
        if not self.min_stack:
            self.min_stack.append(val)
        # min_stack isn't empty actually contain values
        else: 
            self.min_stack.append(min(val , self.min_stack[-1]))
            


        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]





        
