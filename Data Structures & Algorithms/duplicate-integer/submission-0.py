class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Idea: Sorting (while not preserving order) then looping and comparing
        
        A- Solution Complexity 
            Time Complexity: O(n log n) because of sorting
            Space Complexity: O(1)  --> used sort method which preserves the orignal list not need to create a new list to sort it
                            

        B- Difference between sorted(list) and list.sort()
            list.sort() - modifies the list in-place, returns None
            sorted(list) - returns a new sorted list, leaves original unchanged
            Note: Your sorting solution is excellent when you don't need to preserve the original array order
        '''
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False