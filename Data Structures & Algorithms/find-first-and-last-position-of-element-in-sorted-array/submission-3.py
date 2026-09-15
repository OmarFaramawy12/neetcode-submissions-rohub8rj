class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Main IDea: Binary Search over the Array
            - Returning the firrst Occurrence and Last occurence of a given element
            - Compute the Middle Element -> mid = (left + high) / 2 (even case vs odd case)
            - Comaprare the target value with mid:
                1- target > arr[mid]:
                    - discard the left side
                    -increment mid to be mid+1
                2- Target < arr[mid]:
                    - dicard the right side of array
                    - make high = mid
                3- Target Found (we still yet don't know whete the last and first occcurence)
                    - Nb: leftBias is boolean flag as it is aasserting we may find an answer in left Subaarry
                    - false: assering: we may find answer in the right subarray

                    Main IDea: Even if we found the target:
                        - we want to search again in left space and riht pace
                    
                    Case-1: leftBias is true (ackowledging that we may find another target on left direction)
                        a- search the left part + discard the right part -> (right = mid-1)
                    

                    Case-2: Left Bias is False (acknowledging that we may find another value in right range):
                        b- search in right range + discard the left part (left = mid-1)


                    Note:  Rehorical ;Qiestipoim:
                        Q: Is it guranteed that when we discard the mid for first time (classic binrary search)
                        to Apply Binary Search Again on the left portion of array and right porion of Array, 
                        that we find the first mid we discarded?
                            ansWer: yes -> due when searching left or right again
                            we  gurante that we will land on the same first middle again
       
        '''

        # Main IDea: Run the Binary Search 2 Times (once-> LeftBias is True) + (Once -> Right Bias is false)
        left_pointer = self.binarySearch(nums , target , leftBias = True)
        right_pointer = self.binarySearch(nums , target , leftBias = False)
        return [left_pointer , right_pointer]
    

    # helper Function:
    def binarySearch(self , nums , target , leftBias):

        left , right = 0 , len(nums)-1
        i = -1

        while left <= right:
            # to prevent Overflow
            mid = left + (right-left) // 2

            if target > nums[mid]:
                # discard left portion
                left = mid + 1
            elif target < nums[mid]:
                #discard right portion
                right = mid - 1
            else:
                # Target Foufnf
                i = mid # to save mid beause itwill be updated
                if leftBias:
                    # Searchj again in the left portion (discard the right portion)
                    right = mid - 1
                else:
                    # Right Bias (searching in right portion) -> (discarding  the ledt porion)
                    left = mid + 1
        return i
                    
         





