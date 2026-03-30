class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # build the three arrays
        prefix = [0] * n
        suffix = [0] * n
        result = [0] * n

        # set some constants
        prefix[0] = suffix[n-1] = 1

        # 1- Loop over the prefix array and compute it
        # we begin from 1 because the prefix[0] is already 1 nothing before the first element
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        # 2- loop over the suffix array and compute it
        # we begin from n-2 because (n-1) is already equal 1 (nothing after the last element)
        # -1 second argument: -1 exclusively means we reach 0 inclusive
        # -1 third argument: going backwards
        for i in range(n-2 , -1 , -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        #3- compute the reuslt
        for i in range (n):
            result[i] = prefix[i] * suffix[i]

        return result