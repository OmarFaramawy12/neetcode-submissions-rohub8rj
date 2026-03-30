'''
Main Idea:
    1- Remove all the Non AlphaNumeric Characters from the string by using:
        A- Regular Expressions using the re module
            re.sub(pattern , replacement, string)
        B- using the .isalnum() method with  generator expression (overhead)
            this requires looping over the characters and check if each character is alphanumeric
            then join all the alphanumeric characters into one string
    2- Using the Two pointer Technique
'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove all the Non AlphaNumeric characters from the string using regular expression
        subistuted_s = re.sub(r'[^a-zA-Z0-9]' , "" , s).lower()
        print(f"Subistuted String is : {subistuted_s}")
        #Applying the Two Pointers Technique
        left = 0
        right = len(subistuted_s) - 1

        while left <= right:
            if subistuted_s[left] == subistuted_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


        

        