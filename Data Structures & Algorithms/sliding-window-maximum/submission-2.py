class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Algorithm: (Monotonic Decreasing Stack) + fixed-size sliding window
            - usage of Monotonic Decreasing Stack
            - Loop over the array once using the sliding window technique -> O(n)
            - Every fixed size k window:
                a- make test for every given element in the window with top of stack: nums[r] >= stack[-1] 
                b- test succeded: -> pop all the elements from the stack (where new element beats up)
                c- Test failed: -> join the new element to the waiting list
            left pointer got updated -> a- reaches the end of the k (r-l+1) > k

        Time Compexity: O(n)
        Space Complexity: O(n)

        '''
       # res = [2,2,4,4,6]
       #          0   1   2   3   4   5   6
       # nums = [ 1 , 2 , 1 , 0 , 4 , 2 , 6 ],       k = 3       stck = [6],     # indices
        #                         l   l   r

        res = []
        queue = collections.deque()
        left = 0

        for right in range(len(nums)):
            # case Test Case Succeed
            while len(queue) > 0 and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)

            if left > queue[0]:
                queue.popleft()

            if (right - left + 1) >= k:
                res.append(nums[queue[0]])
                left +=1
            
        return res