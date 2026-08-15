class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Sliding Window Technique (Fixed-size sliding window): 
        Problem Statement: No of Something Constraint
            - Given: Array/String + max_window_size = k
            - Required: find the fixed-subarray that contains exactly 2 duplicates in the given fixed-size window
            - loop 
            - if window size reached size k:
                a- remove the nums[left] from hashset
                b- shrink the window fromm left -> left +=1
        '''

        
        left =0
        window = set()

        for right in range(len(nums)):
            if nums[right] in window:
                return True

            window.add(nums[right])
            
            if len(window) > k:
                window.remove(nums[left])
                left +=1

        return False