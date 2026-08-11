class Solution:
    '''
    [1 , 1 , 2 , 3 , 4 ]
    [2 , 10 , 10 , 30 , 30 , 30 ]                   seen  = (2 , 10,  30) -> arr,remove(arr[left]) - > O(n)
     l   r                                              # after removing from array-> check left again (due shifting array)
         l    r
              l     r
    [2 , 10 , 30 , 30 , 30 ]                        arr.remove(left)
                    l    r          
    [2 , 10 , 30 , 30 ]  
                    l
    '''
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()
        left = 0 
        while left < len(nums):
            if nums[left] not in seen:
                seen.add(nums[left])
                left +=1
            elif nums[left] in seen:
                nums.pop(left)

        return len(nums)
        