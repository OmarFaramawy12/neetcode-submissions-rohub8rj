class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) - 1
        max_area = float('-inf')
        
        while left  < right:
            width = min(heights[left] , heights[right])
            length = right - left

            area = width * length
            max_area = max(area , max_area)

            # Step-2: Updating the Pointers 
            if width == heights[left]:
                left +=1
            elif width == heights[right]:
                right -=1
        
        return max_area