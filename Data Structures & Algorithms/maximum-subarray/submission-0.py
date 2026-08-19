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
            I - Loop over the entire array once  + compute sum -> O(n)
            II- Loop over the array for second time using two pointer technique (sliding window) -> O(n)
            Time Complexity:
                - O(n) + O(n) -> O(2n) = O(n)
            Space Complexity:
                - O(1)


        '''
        
    #nums =  [ 2 , - 3 , 4 , -2 , 2 , 1 , - 1 , 4 ]          total_sum = 7    curr_sum = 3     max_sum = max(7,8) = 8
    #         l          r     
              #[  -1 ]                   total_sum = -1          curr_sum = -1     max_sum = max() = -1          

        # Step-1: Compute the Sum of the whole array
        total_sum = 0
        for num in nums:
            total_sum += num

        # step-2: Apply Sliding window Technique or Two Pointers
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
















