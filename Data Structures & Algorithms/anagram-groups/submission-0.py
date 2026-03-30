class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1- sort the List while not preserving the list (create an auxilaru space)
        sorted_strs = []
        for i in range(len(strs)):
            sorted_strs.append("".join(sorted(strs[i])))
        print(sorted_strs)
        
        #2- create a dictionary of the sorted list
        dictionary = {}
        for i in range(len(sorted_strs)):
            key = sorted_strs[i]
            if key not in dictionary:
                dictionary[key] = []
            dictionary[key].append(strs[i])
        print(dictionary)
        
        #3- Return a list for the values of the dictionary
        return list(dictionary.values())