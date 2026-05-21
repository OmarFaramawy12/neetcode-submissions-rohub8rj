class Solution:
    '''
    Brute Force Solution:
        1- Time Complexity: O(n^2)
        2- Space Complexity: O(1) 
        Note: List returned size doen't grow with input size 
        - It only contains 2 numbers
        - Constant time Space Complexity

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):          #O(n)
            for j in range(i+1,len(nums)):  #O(n)   
                if nums[i] + nums[j] == target: #O(1)
                    return [i,j]                #O(1)
        return []                               #O(1)
        