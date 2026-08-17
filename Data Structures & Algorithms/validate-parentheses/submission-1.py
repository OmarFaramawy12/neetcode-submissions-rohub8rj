class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Solution: Stack
            - have hashmap -> maps the openeing bracket to the closing bracket
            - loop over the string
            - if encountered any openeing bracket -> append to stack
            - encountered any closed bracket:
                a- check it's openeing brackets + closed bracket from Hashmao
                b- if they match: -> pop from stack
            - returning true -> stack at the end is empty (not stack = True --> Stack is empty)

        I- Time Complexity:
            - O(n)
        II- Space Complexity:
            - O(n) -> Stack only contains the openingof brackets (original probems contain only open bracekts with
                with no closing brackets at all)
        '''
        
        stack = []
        dictionary_map = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        open_brackets = dictionary_map.keys()

        for char in s:
            # Case Open brackets
            if char in open_brackets:
                stack.append(char)
            # case: Closed Bracket
            elif char in dictionary_map.values():
                if not stack:
                    return False
                top_element = stack.pop()
                if dictionary_map[top_element] != char:
                    return False
        return not stack
                

            
                