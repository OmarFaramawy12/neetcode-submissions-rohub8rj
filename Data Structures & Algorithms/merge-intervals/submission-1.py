class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        '''
        Determininng the Overlapping:
            - Idea: Don't use extra space for every overlapping interval by making new merged 
            list (Space Complexity)
            - having a result list -> mutate the output list (instead of creating new interval for each merged list)
            I- Case-1: Overlapping Occur ifs ->  L[1] >= R[0] (R[0] <= L[1])
                1- Mutate the output list by changing only the end number in the previous interval 
                - > L = [L[0] , R[1]] or result[-1][1] = max(lastend , end) 
                2- Append Interval to the Result  
                Note: Idea of max -> suppose that we have 2 overlappping intervals [1,5] [2,4]  
                - overlapped interval must be -> [1,5] not [1,4]
                - without max -> the overlapped interval will be [1,4] actually we shrinked the interval

            II- Case-2: No Overlapping Occurs
                - Append the inteval as it is in result

            III- Algorithm Complexity:
                -Time Complexity:
                    - Sorting: O(nlogn) in worst case due TimeSort
                    - Interval[1:] -> creates a shallow copy in memory (copying with reference) -> O(n)
                    - Total Complextiy: -> O(nlogn + n) -> at large >> n 
                    -Total Complexity -> O(nlogn)

                -Space Complexity:
                    - O(n): Time sort uses an additional array for merging in worst case
                    - Result: output list O(n)
        '''


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