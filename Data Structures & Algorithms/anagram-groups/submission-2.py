from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        sorted_list = []
        result = []
        # sorting each string in the list lexicograpghically
        for string in strs:
            sorted_text = "".join(sorted(string))
            sorted_list.append(sorted_text)
        
        for index, string in enumerate(sorted_list):
            res[string].append(strs[index])
        
        print(res)
        for valu in res.values():
            result.append(valu)
        return result
        
        