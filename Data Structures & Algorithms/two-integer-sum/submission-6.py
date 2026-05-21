class Solution:
    '''
    Optimal Solution: Two Pointer + Sacrificing Space Complexity

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1- create a hashmap
        # Store all indices for each value to handle duplicates
        hashmap = defaultdict(list)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)

        #3- Apply Two Pointer Approach
        sorted_nums = sorted(nums)
        left , right = 0 , len(nums)-1
        while left < right:
            current_sum = sorted_nums[left] + sorted_nums[right]
            if current_sum == target:
                i, j = hashmap[sorted_nums[left]].pop(0), hashmap[sorted_nums[right]].pop(0)
                return sorted( [i, j] )
            elif current_sum > target:
                right -=1
            else:
                left +=1
        return[]