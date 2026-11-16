class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Main Idea => using rolling hash-set + sliding window technique
        Algorithm:
            - using the rolling hash-set to avoid duplicated work
            - Traversing the array is done by right pointer, while having the left pointer at the beginning
        '''

        seen = {}

        for index , num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff] , index]
            seen[num] = index