class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        result = []
        intervals.sort(key = lambda i: i[0])
        result.append(intervals[0])

        for start , end in intervals[1:]:
            # Case-1: Overlapping Occur + (No Incrementing right / left pointer)
            lastEnd = result[-1][1]            
            if start <= lastEnd:
                result[-1][1] = max(lastEnd , end)

            # Default Case: No Overlapping Occur (increment left pointer)
            else:
               result.append([start , end])

        return result