class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Main Algorithm: -> Kadans Algorithm
            - Core Idea: 
                I- unlike the Max Sum SubArray -> where any running negative  summation won't
                 contribute to the largest sum of the entire subarray.
                
                II- Dealing with Products deals with two main cases
                    A: Case-1 -> The Entire Array contain large positive numbers (trivial)
                        - In this case the maximum product will be the product of all positive 
                        numbers

                    B: case-2 -> The Array contain all negative Numbers:
                        - negative numbers flip & alternate the sign 
                        - (+ve) * (-ve) -> result is (-ve)
                        - (-ve) * (-ve) -> result is (+ve)
                        - main theme: 
                            1- keep track of both the maximum product so far(ending at given
                             position in the array)
                            2- Keep Track of the Minimum Product so far(ending at given
                             position in the array)
                            3- Reason: if the Current proceesed number in array is negative 
                            multiplied by the worst streak negative product -> yields largest
                            positive value (as result)
                           


                III- Tweak in Algorithm:
                    - previously (in max sum subarray) -> we discard the negative current 
                    running sum (by resetting the curr_sum back to zero -> start new window)
                    - In this case we will do the similar but by using the max and min operation with 3 variables (curr_max, curr_min, number itself)


                IV- Algorithm Complexity:
                    1- Time Complexity: -> O(n) -> Kadans Algorithm
                    2- Space Complexity: -> O(1):
                        maintaiing only 3 variables that doesn't grow with input size



                - num * curMax (old) Candidate: extend the previous best streak with num
                - num * curMin (old) Candidate: extend the previous worst streak with num
                this is what lets a negative num flip a bad streak into a good one
                - num alone Candidate: abandon everything, start a fresh subarray at this
                 position tmp	A snapshot of num * curMax (old), saved only because curMax is
                  about to be reassigned and curMin's formula still needs that old value
        '''


        curr_max , curr_min = 1 , 1
        max_product = max(nums)

        for num in nums:
            # To keep Track of the running product only
            temp = num * curr_max
            curr_max = max(num*curr_max , num*curr_min , num)
            curr_min = min(temp , num * curr_min , num)

            max_product = max(max_product , curr_max)

        return max_product
        


           





























