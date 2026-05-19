class Solution:
    '''
    I- Algorithm Complexity:
        1- Time Complexity: O(n)   #looping over the array once
        2- Space Complexity: O(1)
        Note: This Algorithm will make alot of unwanted Copying in case of nums[left] != val
              for a very large arrays (only few elements would be removed)
                    Example: [3,2,5,1,7,8,9,10,11,12,13,3,14,15,16,17,18,19,20,3] 
                         - In this case will make 17 copies (overwriting) to remove 3 (pratically will remove only the first 3)
    II- More effiecient Solution is provided as
    
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        right = 0   #O(1)
        for left in range(len(nums)): #O(n)
            if nums[left] != val:     #O(1)
                nums[right] = nums[left]    #O(1)
                right +=1                   #O(1)

        return right                        # O(1)

    
    