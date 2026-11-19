class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # constrcuted set -> O(n)
        new_nums = set(nums)
        # maintain the length of longes sequence among all sequences
        longest_seq = 0
        # length: length of the running sequence (got reset with the beigning of new 
        # sequence)
        length =0 

        for i in range(len(nums)):
            # Q: is the number considered beginning of seqience ?
            # case-1: start of sequence
            if (nums[i]-1) not in new_nums:
                length = 1
                # next number exist in set
                while (nums[i]+length) in new_nums:
                    length +=1

                longest_seq = max(longest_seq , length)

        return longest_seq



