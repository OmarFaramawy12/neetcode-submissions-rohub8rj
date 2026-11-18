class Solution:

    '''
    Decode Algorithm Main explanation:
                            0   1   2   3   4   5   6   7   8   9   10  11  12  13
        encoded_string: "   5   #   h   e   l   l   o   5   #   w   o   r   l   d   "

                            i   j   j+1                 tr

    '''

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        print("Encoded String" , res)
        return res


    def decode(self, s: str) -> List[str]:
        # indicate: delimiter is begining of new word

        res , i = [] , 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            res.append(s[j+1: j+ 1 + word_length])
            # update index i
            i = j + 1 + word_length


        return res








       