import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        MAin Idea of ALgorithm:
            - Recall Binary search requires array is sorted in Ascending order
            - Rotated Array: 
                a- Portion-1 Sorted Ascending
                b- Portion-2 Sorted Ascending
                c- Portion-1 + Portion-2 -> Exist pivot (transitioning point) where:
                    - numbers will be decreasing (not sorted any more)
                    - Pivot Point -> beginning of portion-2 sorted array

                d- Trick: Mnimimum Number will exists at the beginning of the portion-1 or 
                portion-2 

            I- Algorithm Cases:
                A- Case-1: nums[mid] <= nums[right]:
                    - this case describe that array is sorted already ascendigly (increasing order)
                    - minimum variable must be at the first rotated half where it contain the 
                    smaller values
                    - Search the left portion of Rotated array:-> right = mid - 1
                
                B- Case-2: nums[mid] > nums[right]:
                    - case where the first portion of array is increasing order, where means that   
                    numbers will decrease (going into other portion of array where it contain smaller 
                    values)
                    - Search the second poriotn of array (smaller values) -> discard the left portion
                        a- left = mid + 1

            III- Time complexity: O(logn) -> Binary Search
            IV- Space Complexity: O(1):
                - maintaining oly some pointers (left , right ) and variable (min_so_far)
        

        '''
       
        left , right = 0 , len(nums) - 1
        min_so_far = nums[0]

        # Edge Case (Default value): Array isn't rotated (normal sorted ascending order array):
        

        while left <=  right:

            if nums[left] < nums[right]:
                return min(min_so_far , nums[left])

            mid = left + (right - left) // 2
            min_so_far = min(min_so_far , nums[mid])
            # Case-: array is increasing (minimum must sit on left) -> discard the right portion
            if nums[right] >= nums[mid]:
                right = mid - 1
            # Case: nums[mid] > nums[right] -> array will be decreasing (smaller elements are on 
            # left) -> discard the left porion of array
            else:
                left = mid + 1

        return min_so_far 












