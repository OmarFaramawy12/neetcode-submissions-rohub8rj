class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        MAin Algorithm: TraditionalBinary Search

            - Main-Idea: Elimination half of the search space (Keep Dividing the Search     
            Space by 2)

            -Time Complexity: -> O(logn)
            -Space Complexity: -> O(1) maintaining only pointers
        '''

        left , right = 0 , len(nums) - 1
        while left <= right:
            # to prevent Overflow
            mid = (left+right) // 2
            if target > nums[mid]:
                # Discard the left portion of Array
                left = mid + 1
            elif target < nums[mid]:
                # Discard the right Portion of Array
                right = mid - 1
            else:
                return mid

        return -1