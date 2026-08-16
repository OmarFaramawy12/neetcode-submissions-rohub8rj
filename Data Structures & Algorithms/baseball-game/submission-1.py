class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        Stack: 
            0- Reason for choosing stack -> all operations is O(1) + Searching O(n)
            1- append operation if any string integer
            2- "+" encountered -> sum two previous element in stack
            3- "C" -> pop last element from stack
            4- "D" -> insert (double of last element in stack):
                a- peep over the stack
                b- double it
                c- insert it in stack
        '''
        #ops = [ "1" ,   "2" ,   "+" ,   "C" ,   "5" ,   "D" ]   stack = [1 ,2, 5, 10]
        

        stack = []
        for i in range(len(operations)):            
            match operations[i]:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1] * 2)
                case _:
                    stack.append(int(operations[i]))    
        return sum(stack)


                



