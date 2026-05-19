class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left , right = 0 , len(nums) - 1
        # stopping condition is 1- left > right or left == right
        while left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -=1
            if nums[left] != val:
                left +=1

        return left
        