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
            - right < left -> 
                a- min (mid , right)
                b- discard the left poriotn of array (min in right)
            - right > left -> 
                a- min(l,m)
                b- discard right portion of array (min in left)
            - keep track of min variable 

            right >= mid (array is incresing): -> search in left space for min (min must be before 
            this element):
                a- right = mid - 1
            -right < mid: (we know that smaller elements are on the right of the array):    
                discard the left subarray: -. left = mid + 1


                    0       1       2       3       4       5
        nums = [    3   ,   4   ,   5   ,   6   ,   1   ,   2   ]   mid = 1 min = 1
                    l               m       lmr       m         r
                


                    0       1       2       3       4       5
        nums = [    4   ,   5   ,   0   ,   1   ,   2   ,   3   ] mid = 4   ,    min= 1
                    l               m       lmr       m        r



min_so_far = 0 min(min_in_range , min_so_far)

        '''
       
        left , right = 0 , len(nums) - 1
        min_so_far = nums[0]

        while left <=  right:

            mid = left + (right - left) // 2
            min_so_far = min(min_so_far , nums[mid])
            # Case-: array is increasing (minimum must sit on left) -> discard the right portion
            if nums[right] >= nums [mid]:
                right = mid - 1
            # Case: nums[mid] > nums[right] -> array will be decreasing (smaller elements are on 
            # left) -> discard the left porion of array
            else:
                left = mid + 1

        return min_so_far 












