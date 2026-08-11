class Solution:
   
    '''
    nums = [2, 10 , 10 , 30 , 30 , 30 ]
                l    r    r
                r    
    Solution-2: No shifting (Optimal)
    - left = 0 , right = left +1
    - left and right pointer moves with each other
    - left pointer denotesthe place where we will tore the next unique element
    - right pointer only scan through the array
    - compare right with previous element if they are unqual: -> swap the element at the right index with the index left
                                                              -> 2- Increment left
    
    - return the (left) -> indicating the number of unique elements in the array
    Time Complexity:
        - O(n)
    Space Complexity: 
        - O(1)
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = 1
        for right in range(1 , len(nums)):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left +=1
        return left


       


        