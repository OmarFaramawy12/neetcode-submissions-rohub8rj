from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = Counter(s)
        hashmap_t = Counter(t)

        return hashmap_s == hashmap_t