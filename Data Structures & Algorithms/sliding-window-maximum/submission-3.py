class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Algorithm: (Monotonic Decreasing Stack) + fixed-size sliding window
            - usage of Monotonic Decreasing Stack
            - Main Idea:
                I- we want to remove useless comparisons in every iteration 
                II- Instead of stack -> we will use a queue:
                    a- to allow pop from front -> O(1)
                    b- pop from end -> O(1) (Note: Stack allows only poping from end)
            - Loop over the array once using the sliding window technique -> O(n)
            - Every fixed size k window:
                a- make test for every given element in the window with top of stack: 
                    nums[r] >= stack[-1] 
                b- test succeded: -> pop all the elements from the stack 
                    (where new element beats up)
                c- Test failed: -> join the new element to the waiting list
            - left pointer got updated when reaching the end of current window size

        Time Compexity: O(n)
        Space Complexity: O(n) -> cause the using of the Stack (Queue)
        '''


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




        