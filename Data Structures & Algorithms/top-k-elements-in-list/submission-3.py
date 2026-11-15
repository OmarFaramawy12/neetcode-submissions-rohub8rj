from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''
        Main Idea:
            Step-1: Loop over the nums array and create     
            frequency counter for each element in the array

            Step-2: Obtain an additional array
                - append the hashmap element in the array
                - aim: To be able to sort them
                - Note: we want to sort using the value (frequency counter) not the hashmap 
                key
            Step-3: pop from the end of the array 
                - Main idea: we know that the array is sorted 
                from the previous step, so the largest values 
                exist at the end of the array
                - loop over k elements only and pop them
        '''
        # Step-1: creating the hashmap
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        # Step-2: Sort the additional array
        arr = []
        for key , val in counter.items():
            arr.append([val , key])     # sorting is done using the first argument (er)

        arr.sort()

        # step-3: Loop over the sorted array and pop the k 
        #element only
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res

    

        

