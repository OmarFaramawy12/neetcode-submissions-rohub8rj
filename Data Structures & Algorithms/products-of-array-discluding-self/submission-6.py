class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix , postfix = [0] * n , [0] * n
        prefix[0] = nums[0]
        postfix[n-1] = nums[n-1]
        res = [0] * n
        
        # construct thhe prefix array
        for i in range(1 ,n):
            prefix[i] = prefix[i-1] * nums[i]
        
        # construct the posfix array
        for i in range(n - 2 , -1 , -1):
            postfix[i] = postfix[i+1] * nums[i]
        
        # construct the result

        for i in range(n):
            left_prefix = prefix[i-1] if i > 0 else 1
            right_postfix = postfix[i+1] if i < n-1 else 1
            res[i] = left_prefix * right_postfix


        return res

        

         
        