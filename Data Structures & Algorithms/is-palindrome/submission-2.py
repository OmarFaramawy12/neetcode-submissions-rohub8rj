import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Two pointer Technique:
            step-1: Remove any character that is non-alphanumeric
            step-2: apply two pointers technique

        '''
        s =  re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        left , right = 0 , len(s) - 1

        while left <= right:

            if s[left] != s[right]:
                return False
            
            left +=1
            right -=1


        return True
        

