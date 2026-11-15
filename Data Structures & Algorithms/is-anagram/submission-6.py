class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Algorithm Idea:
            - principle idea -> Each increment count for a character in 
            String S is accompanied by a decrement in count of the same 
            character in String t
            -Two Strings are anagrams: Count array (26 letter) reaches zero
            - if count array at the end not zero: -> there exist characters 
            in String S with more character frequency than string T
        Time Complexity: O(n+m)
        Space Complexity: O(1)
        '''
        if len(s) != len(t):
            return False
        # bounded by the lowercase english letters (only 26 letters)
        counter = [0]*26

        for i in range(len(s)):
           counter[ord(s[i]) - ord('a')] += 1
           counter[ord(t[i]) - ord('a')] -= 1

        for val in counter:
            if val !=0:
                return False
        return True



        