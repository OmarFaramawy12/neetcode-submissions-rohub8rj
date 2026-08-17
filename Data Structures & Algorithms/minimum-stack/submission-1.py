class MinStack:
    '''
    Note:
        - underthehood the dynamic array resizes with it self (don't implement the resizing process)
        - getting the minimum require traversing the stack (dynamic array) + retrieve min -> require O(n) traversal
            a- Time Complexity of getting min: -> O(n)
        - Exist an optimized approach, where required Time Complexity -> O(1):
            a- having another stack that keeps track of the min 
            b- main objective: min resides at the top of stack
            c-this will ensure the following operations:
                I- pushing to stack
    '''
    def __init__(self):
        # initialize a new dynamic array
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)  # O(1)
        # Inner line: comapre the value with top element of min stack (if it contain elements) 
        '''
        if self.minStack: (stack have elements)
            val = min(val, self.minStack[-1])
        else:
            val = min(val, val)   # equivalent to: val = val
        '''
        val = min(val , self.minStack[-1] if self.minStack else val)          
        self.minStack.append(val)
            
        

    def pop(self) -> None:
        self.stack.pop()        #O(1)
        self.minStack.pop()

    def top(self) -> int:   
        return self.stack[-1]        # O(1)
        

    def getMin(self) -> int:
        return self.minStack[-1]        # O(1)

        
