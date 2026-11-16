from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step-1: obtain the frequency counter for both strings
        counter_s , counter_t = {}, {}
        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i] , 0)
        
        for j in range(len(t)):
            counter_t[t[j]] = 1 + counter_t.get(t[j] , 0)

        return counter_s == counter_t




        

        