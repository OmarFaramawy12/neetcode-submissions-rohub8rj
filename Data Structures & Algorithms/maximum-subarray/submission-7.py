class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Main Idea: Avoid Current Negative Sum Running -> wont lead to the greatest summation
        - curr_sum < 0: -> start new window (Kadan's algorithnm)

        '''

        left = 0
        curr_sum = 0
        max_sum = nums[0]       # Assumption array is non-empty

        for right in range(len(nums)):


            '''
            if curr_sum < 0:
                curr_sum = 0
                left = right
            '''
            # Same above cod -> write using the max operation

            if curr_sum < 0:
                curr_sum = max(0 , curr_sum)
                left = right
            
            curr_sum += nums[right]
            max_sum = max(max_sum , curr_sum)
        return max_sum