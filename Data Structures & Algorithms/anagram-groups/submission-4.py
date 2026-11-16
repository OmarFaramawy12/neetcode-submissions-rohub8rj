from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        sorted_list = []
        result = []
        # sort the words alphabetically -> the anagrams will appear one after each other

        for string in strs:
            sorted_word = sorted(string)
            sorted_list.append("".join(sorted_word))

        for index , word in enumerate(sorted_list):
            res[word].append(strs[index])
                   

        for value in res.values():
            result.append(value)
        
        return result


        
        