class Solution:
    def isValid(self, s: str) -> bool:
        # step-1: build hashmap
        hash_map = {

            "(" : ")",
            "{" : "}",
            "["  :  "]"
        }

        # step-2: obtain keys separetly

        keys = hash_map.keys()  # view object
        stack = []

        for char in s:
            if char in keys:
                stack.append(char)
            elif char in hash_map.values():
                if not stack:
                    return False
                top = stack.pop()
                if hash_map[top] != char:
                    return False


        return not stack

        


