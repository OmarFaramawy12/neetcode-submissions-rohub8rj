class Solution:
    def isValid(self, s: str) -> bool:

        ''' 
        Initialize some variables: 
            a- Stack (dynmaic Array)
            b- Dictionary: to map every openening bracket with it's coreesponding closed
                bracket
        '''

        stack = []
        dictionary_mapping = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        # we need to know which are the opening brackets which are the keys of the dictionary
        open_brackets = dictionary_mapping.keys()
        # loop over every character of the string
        for char in s:
            # check if character is an open bracket
            if char in open_brackets:
                # append it to stack
                stack.append(char)
            # checking if it is closed bracket
            elif char in dictionary_mapping.values():
                if not stack:
                    return False
                
                last = stack.pop()
                if dictionary_mapping[last] != char:
                    return False
        return not stack







        