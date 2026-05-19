class Solution:
    '''
    Algorithm Complexity:
        1- Time Complexity: O(n)   #looping over the array once
        2- Space Complexity: O(1)
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        right = 0   #O(1)
        for left in range(len(nums)): #O(n)
            if nums[left] != val:     #O(1)
                nums[right] = nums[left]    #O(1)
                right +=1                   #O(1)

        return right                        # O(1)

    
    