'''
Algorithm: Using Counter Class
    a- Counter class counts number of elements of any iterable
    b- returns a dictionary conatining key-value pairs returning the frequency of each iterm (HashMap)
    c- loops only on the character to count the frequency of each element --> O(s) or O(n) where s, n
        are the number of charcters in the string

    Time Complexity: O(n)
    Space Complexity: O(k), where K is the number of unique characters stored in hashmap (Dictionary)
'''


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_S = Counter(s)  # O(n)
        counter_T = Counter(t)  # O(m)
        if len(s) != len(t):    #O(1)
            return False
        return counter_S == counter_T # O(k1+k2) <= O(n+m) = O(2m) = O(m)

    # Time Complexity: O(n+m) --> general Case
    # Space Complexity: O(k1+k2) where k1,k2 are the number of unique charracters stored in both strings respectively
    # Constraint that k <= 26 --> so space Complexity is O(26) which is constant time --> O(1)
