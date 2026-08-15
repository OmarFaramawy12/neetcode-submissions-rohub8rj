class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        - Looping will be with right pointer:
            a- check the window size if > k:
                - decrease the total -= arr[left]
                - shrink the window size -> increment left pointer
            b- Case: still valid window -> add the number of right to total
        - (shrink window size): Increment left pointer -> when reaching size of k 
        - maintain the resulted subarray -> counter or Hashmap
        

        '''


       
        left = 0
        counter , total = 0 , 0

        for right in range(len(arr)):
            #curr_size = right - left + 1
            # If current window size > k: -> shrink the window from left (increment the left pointer)
            if (right - left + 1) > k:
                total -= arr[left]
                left +=1

            total += arr[right]

            if (right - left + 1) == k:
                avg = total / k
                if avg >= threshold:
                    counter +=1

            
           
        return counter
            

          