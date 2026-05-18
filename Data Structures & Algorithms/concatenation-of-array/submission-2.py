class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2*length)       
        # making deep copy for the ans
        # copying first n elements
        for i in range(len(nums)):
            ans[i] = nums[i]
        j = 0
        for i in range(length, len(ans)):
            ans[i] = nums[j]
            j +=1
        return ans

        