class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        '''
        Brutte Force:
            - loop over the array + for each element 
                a- sum over all the rest element 
                b- record sum & take the maximum
            - retun the max sum seen so far
            I - Time Complexity: -> O(n^2)
            II- Space complexity: -> O(1)

        Second : Optimized approach
            I- Loop over the array for second time using two pointer technique (sliding window) -> O(n)
                - curr_sum: represents the current sum of all the elements in the given window
                - Main Idea: a- if curr_sum becomes negative value -> we don't want to add negative values at all
                             b- negative values -> decreases the sum
                             c- encountered negative values:
                                1- reset the curr_sum back to 0
                                2- update the window to point (left = right)
           
            Time Complexity:
                - O(n)
            Space Complexity:
                - O(1)


        '''
        
    
       
        # step-1: Apply Sliding window Technique (Growing Sliding Window)
        max_sum = nums[0]
        curr_sum =  0
        left , right = 0,0 

        for right in range(len(nums)):
            if curr_sum < 0:
                curr_sum = 0
                left = right
            curr_sum += nums[right]
            max_sum = max(max_sum , curr_sum)
        return max_sum
















