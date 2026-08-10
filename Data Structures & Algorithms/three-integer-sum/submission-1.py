class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        [-1 , -1, 0, 1 ,2 ,4]
        result = set()
        # sorting the input array in place
        nums.sort() # O(nlogn)
        for i in range(len(nums)-2):
            left , right = i+1 , len(nums) - 1
            while left < right:
                total_sum  = nums[i] + nums[left] + nums[right]
                if total_sum == 0:
                    result.add((nums[i] , nums[left] , nums[right]))
                    left +=1
                    right-=1
                elif total_sum < 0:
                    left +=1
                else:
                    right -=1
        return [list(t) for t in result]
                