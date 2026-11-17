from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Main IDea: 
            - Have an array (bucket sort), where the indices of the array are length of the array
            - Goal: map each number in the original array to it's frequency (array indices)
            - think of it as bucket where each value goes to it's own bucket

        '''
        counter = defaultdict(int)
        for num in nums:
            counter[num] = 1 + counter.get(num , 0)

        freq_bucket = [[] for i in range(len(nums) + 1)]

        for key,value in counter.items():
            freq_bucket[value].append(key)
        res = []
        for i in range(len(freq_bucket) - 1 , 0 , -1):
            for j in freq_bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res
                    
          
    
        
       
        