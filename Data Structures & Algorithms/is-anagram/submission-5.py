from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Idea: 
        First: Using The Hasmap (Counter Dict):
            - Hashmap is unordered DS
            - Ordering doesn't matter in the problem, 
            - aim: we care about the count of the characters
                   where the two strings must maintain the 
                   same character frequncy 
            II- Algorithm Complexity:
                - Time Complexity: comparing the Two hashmaps are O(n)
                - Space Complexity: O(k1) , O(k2), where they are two
                hashmaps contiaing the unique characters for each 
                string 
        '''

        counter_s1 = Counter(s)
        counter_s2 = Counter(t)
        return counter_s1 == counter_s2


        


