class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        '''
        MainIdea: Limited down to fixed alphabet size (Lower case 
        only -> 26 letters (constant space))
            - Usage: Fixed size constant array (never grows with  input)
            - Loop over the main string s:
                1- for each character in s increment the frequency 
                coounter of it
                2- at  the same time: decrement the freqency 
                counter of the same position in the string t
        Big Conclusion: 2 Strings are anagram if the 26 character 
        arrays counts are all zero's
            - that means that each character in s and in t will be incremented and decremented once resulting in zero effect
            - if one string contain more letters than the others 
            (letters that aren't present in the other), there will 
            another numerical value (other than zero) for the 
            addiotnal character in either string
        '''
        if len(s) != len(t):
            return False
        counter = [0] * 26

        for i in range(len(s)):
            counter[ord(s[i]) - ord('a')] += 1
            counter[ord(t[i]) - ord('a')] -= 1




        return all(val == 0 for val in counter) 
