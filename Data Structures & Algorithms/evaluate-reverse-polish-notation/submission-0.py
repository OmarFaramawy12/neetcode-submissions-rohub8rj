class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Problem Formulation: -> will be uisng Stack to account for the operands
            a- loop over the array until find an operator
            b- oush to stack if operand
            c- found an operator -> pop from stack and apply the operator to poped elements
            d- push result to stack
            e- algorithm will finish when stack is emepty (or finished looping over the array)
        
        I- Time Complexity: -> O(n)
        II- Space Complexity: -> O(n) 
            - Space Complexity is O(n) due using of stack
        '''
         #tokens = ["1" , " 2 " , " + " , " 3 " , " * " , " 4 " , "  - " ]          stack = []


        stack = []

        for i in range(len(tokens)):
            # Step-1: as tokens[i] not an operator (is an operand) -> push to stack
    
            # Step-2: Encountered an operator -> a- pop from stack (until empty) 
            #                                    b- apply the operator to the elements in stack
            match tokens[i]:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    b,a = stack.pop() , stack.pop()
                    stack.append(a-b)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    b , a = stack.pop() , stack.pop()
                    stack.append(int(a/b))
                case _:
                    stack.append(int(tokens[i]))
        return stack[-1]
          


       