class Solution:

    def encode(self, strs: List[str]) -> str:
       
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result
        
    
    def decode(self, s: str) -> List[str]:

        result, i  = [] , 0
        while i < len(s):
            j = i
            # J will exit when it is equal t delimiter (#)
            while s[j] != "#":
                j +=1
            word_length = int(s[i:j]) # j won't be included because j will be pointing to delimiter
            result.append(s[j+1 : j + 1 + word_length])
            # update index to account for the beginning of new length of the new word
            i = j + 1 + word_length
        return result

