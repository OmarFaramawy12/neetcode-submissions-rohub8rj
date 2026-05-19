class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = 0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                max_right = max(max_right,arr[j])
            arr[i] = max_right
            max_right = 0
        arr[len(arr)-1] = -1
        return arr


        

