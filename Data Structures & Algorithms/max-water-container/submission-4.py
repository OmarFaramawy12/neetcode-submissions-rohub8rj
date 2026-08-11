class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Two Pointers Technique
            - maximizing the area require maxisimizing both length and Width:  
                1- will make us start the left pointer at the beginnig & Right pointer at the end (left = 0 , right = n)
                2- objective: maximize height --> will update and move the pointer that have the least height
            - having two bars with heights (6,7) --> 1- choose the the length to be of (height:6)   
                                                     2- otherwise the water will overflow

            - width isthe difference between the two bars
            - Note: array can't be sorted: Required Time Complexity -> O(n)
        '''
        left , right = 0 , len(heights) - 1
        max_area = 0

        while left < right:
            area = abs(right - left) * min(heights[left] , heights[right])
            max_area = max(max_area , area)

            # Step-2: updating pointers
            #objective: maximize height --> will update and move the pointer that have the least height

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                right -= 1 # else case is where the heights[left] = heights[right] --> you can move either the left or right

        return max_area