class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.isdigit():
                stack.append(int(op))
            else:
                match op:
                    case "+":
                        #first_num = stack.pop()
                        #sec_num = stack.pop()
                        stack.append(stack[-1] + stack[-2])
                    case "C":
                        stack.pop()
                    case "D":
                        #first_num = stack.pop()
                        stack.append(2 * stack[-1])
                    case _:
                        stack.append(int(op))
                  
        

        return sum(stack)
