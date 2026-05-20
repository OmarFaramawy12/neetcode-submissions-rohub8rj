from collections import Counter
class Solution:
    '''
    Counter Class
    Algorithm Complexity:
        1- Time Complexity: O(n+m)
            comparing two hashmaps:
               Comparing two dictionaries of size at most 26 is O(1).
               In practice, but in general could be O(k).
               where k is the number of distinct characters.
               Since k ≤ 26 (lowercase letters), it's effectively constant.

        2- Space Complexity: O(1)
            The two Counter dictionaries store at most 26 key-value pairs 
            (one per lowercase letter).
            Thus the space used does not grow with the input length .
            it's bounded by the alphabet size, so O(1) auxiliary space.
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = Counter(s)  #O(n): n is the length of string s
        hashmap_t = Counter(t)  #o(m): m is length of string t

        return hashmap_s == hashmap_t   #O(k): where k is number of distinct characters