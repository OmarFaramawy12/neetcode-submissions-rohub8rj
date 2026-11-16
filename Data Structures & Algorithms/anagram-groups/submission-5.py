from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                # obtaining the frequency count
                count[ord(char) - ord('a')] += 1

            # list is mutable (can't be used as key)
            res[tuple(count)].append(string)    

        return list(res.values())