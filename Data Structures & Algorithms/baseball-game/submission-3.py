class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        Algorithm Complexity:
        I- Time Complexity:
            - O(n) -> looping over the array once
            - O(n) -> looping over the stack + computing the sum
            - Total: O(2*n) = O(n)
        II- Space Complexity:
            - best Case: Stack doesn't have any integers - > O(1)
            - average case: stack contain k integers (k<<n) -> O(k)
            - Worst Case: stack contain all integers --> O(n)
        '''
        stack = []

        for op in operations:

            match op:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "C":
                    stack.pop()
                case "D":
                    stack.append(stack[-1] * 2)
                case _:
                    stack.append(int(op))
        return sum(stack)
                    
        