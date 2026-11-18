class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        nums = [2,  20, 4,  10, 3,  4,  5   ]       set =  (2,20,4,10,3,4,5)
                        
        counter = 1

        Main Idea: 
            - at each given number -> we want to check if the number below it exist or not
            - it it doesn't exist -> then this number can start a new sequence
            - if it exist -> then it can't be a start of sequence (must find the number below to start a sequence from)
            - having counter that counts the number of running sequence + resets in the case of can't starting a sequence

        ''' 

        seen = set()
        # Step-1: construct set with numbers eliminating duplciates
        for num in nums:
            if num not in seen:
                seen.add(num)

        # step-2: looping over num and see can start sequence or not
        longest = 0
        for num in nums:
            # case can start a sequence
            if (num-1) not in seen:
                length = 0
                while (num + length) in seen:
                    length +=1
                longest = max(longest , length)
        return longest

        
