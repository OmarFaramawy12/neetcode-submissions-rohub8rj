import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #step-1: remove the spaces from al the string + remove any non-alphanumeric characters
        sub_str = re.sub(r'[^a-zA-Z0-9]' , "" , s).lower()
        
        left , right = 0 , len(sub_str)-1

        while left <= right:

            if sub_str[left] != sub_str[right]:
                return False
            left+=1
            right-=1
        return True
        