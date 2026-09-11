class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Main Idea: -> similar to extracting the max sum subarray
        - Difference -> Max Product can be achieved by two ways: (aka: Exist 2 Cases)
            a- Positive Number can be achieved by:
                1- Multyplying two positive Numbers
                2- Multiplying Two Negative Numbers
            b- 2 Cases:
                I- Case-1: The Array Entries are all positive
                    - Max_Product -> Multiplying all the positive numbers
    
                II- Case-2: Array Entries are all negative:
                    - Recall multiplying two negative numnbers -> yield Positive number
                    - negative sign alternate the multiplicastion
                    - Keep Track of the Most Max Product ever:
                        a- depending on the Number(number<0 & max_product<0) -> positive 
                        product 
                        b- (number>0 & max_product>0) -> positive Product 
                    - Keep Track of the minimum prodcut ever:
                        Keep track of the most negative (minimum) product of the array

        '''


        curr_max , curr_min = 1,1
        max_product = nums[0]

        for num in nums:

            temp = num * curr_max
            curr_max = max(num*curr_max, num*curr_min , num)
            curr_min = min(temp , num*curr_min , num)

            max_product = max(max_product , curr_max)

        return max_product
