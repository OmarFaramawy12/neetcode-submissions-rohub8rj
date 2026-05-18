class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Never modify an iterable when iterating --> lead to skip elements and produce inaccurate results
        '''
        I- Solution: Cloning a list
            a- Shallow Copy:
                1- List Constructor: list() -> list
                2- copy method: copy() -> list
                3- slicing:  original_list[:] -> list

            b- deep copy
                1- Deep Copy method: copy.deepcopy()
        II- Algorithm Complexity:
            1- Time Complexity: O(n) + O(n^2) --> O(n^2)
            2- Space Complexity: O(n) for making a copy of the array
        '''
        # create a shallow copy for the list (here it is primitive Data type) -> shallow copy works fine
        copy_nums = list(nums)      # O(n)
        for num in copy_nums:       # O(n)
            if num == val:
                nums.remove(num)    # O(n)
        return len(nums)
        