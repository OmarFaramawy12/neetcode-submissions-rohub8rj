class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        '''
        arr = [ 1,  2,  4,  6]

        pre = [ 1,  1,  2,  8]
        post= [ 48,  24,  6,  1]

        res = pre[i] * post[i]
        res[0] = pre[0] * post[0] = 1 *  48 = 48
        res[1] = pre[1] * post[1] = 1 * 24 = 24 correct
        res[2] = pre[2] * post[2] = 2 * 6 = 12
        res[3] = pre[3] * [post[3]] = 8 * 1 = 8 correct 
        '''
        n = len(nums)
        prefix , postfix = [1] * n , [1] * n
        product = 1
        # Step-1: compute prefix product 
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]
        # Step-2: Compute Postfix product 
        product = 1
        for i in range(len(nums)-1, -1 , -1):
            postfix[i] = product
            product *= nums[i]

        return [prefix[i] * postfix[i] for i in range(len(nums))]
        