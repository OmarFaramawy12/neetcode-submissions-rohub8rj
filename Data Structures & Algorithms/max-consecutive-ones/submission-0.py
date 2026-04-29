'''
Algorithm Complexity:
    1- Time Complexity: O(n)
    2- Space Complexity: O(1)
'''


from collections import defaultdict
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_counter , curr_counter = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr_counter += 1
            else:
                curr_counter = 0
            max_counter = max(max_counter , curr_counter)
        return max_counter
        
            

                


        