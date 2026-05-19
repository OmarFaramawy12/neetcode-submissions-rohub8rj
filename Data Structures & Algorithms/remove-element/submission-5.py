class Solution:
    '''
    Time Complexity: O(n) * O(n) + O(n) -> O(n^2) + O(n)  --> for  >>>n  Time Complexity: O(n^2)
    Space Complexity: O(n)
    '''
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # make Shallow or Depp Copy in the Primitive Case only doesn't matter
        #slicing method
        nums_copy = nums[:] # Space Complexity & Time Complexity O(n)
        #loop over shallow or Deep Copy + Delete/remove from the Original
        for num in nums_copy:
            if num == val:
                nums.remove(num)    # Time Complexity per element: O(n)
        return len(nums)