from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Construct a Set for storing the triplets
        set_triplets = set()
        # sorting the numbers in place
        nums.sort()

        # starting the Two Pointer Algorithm:
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    set_triplets.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return [list(t) for t in set_triplets]