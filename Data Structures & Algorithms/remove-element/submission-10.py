class Solution:
    '''
    Algorithm Complexity:
        1- Time Complexity: O(n)
        2- Space Complexity: O(1)
        MAin Idea: 
            - Algorithm is more effiecient han solution-3 becauseit do less copies
            - it only copy the leemnt from the end of the array
            - we returned left to return all the elements not equal to value
            - if we returned right --> we will skip an element
    '''
    def removeElement(self, nums: List[int], val: int) -> int:

        left , right = 0 , len(nums) - 1        #O(1)
        # stopping condition is 1- left > right or left == right
        while left <= right:                #O(n)
            if nums[left] == val:           #O(1)
                nums[left] = nums[right]    #O(1)
                right -=1                   #O(1)
            else:                           #O(1)
                left +=1                    #O(1)

        return left
        