class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    # O(1)
            return False
        
        count_s , count_t = {} , {} # O(1)
        # count the frequencies and store them
        for i in range(len(s)): # O(m) or O(n) since they both have the same length
            count_s[s[i]] = 1 + count_s.get(s[i] , 0)   #O(1)
            count_t[t[i]] = 1 + count_t.get(t[i] , 0)   # O(1)
        
        return count_s == count_t # O(k1 + k2) <= O(n+m) = O(2n) = O(2m) = O(n) = O(m)

        #Time Complexity: General Case: O(n+m)
        # Space Complexity: O(k1+k2) where k1 & k2 <=26 --> O(1)
        