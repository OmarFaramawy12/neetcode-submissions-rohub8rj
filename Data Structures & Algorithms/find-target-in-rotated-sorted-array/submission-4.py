class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Main Idea:
        I- Run Two passes of Binary Search
            1- First Pass: => find the pivot where the turning point occurs (beginning of the other half 
            of fully sorted array)
            2- Second Pass: runs classical binary search on each fully sorted halves to find the target 
            value
        '''

        # Step-1: Finding the Pivot

        low , high = 0 , len(nums) - 1

        while low < high:
            mid = low + (high - low) // 2
            # discard the left portion
            if nums[mid] > nums[high]:
                low = mid + 1
            # Case: nums[mid] < nums[high]: discard the right portion
            else: 
                high = mid                 # make the mid itself considered as the pivot


        pivot = low
        
        # step-2: Runs classical binary search on each half
        def binary_search(left: int , right:int) -> int:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:      # discard the  left portion
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1


        result = binary_search(0, pivot-1)
        if result == - 1:
            result = binary_search(pivot , len(nums) - 1)
        
        return result







