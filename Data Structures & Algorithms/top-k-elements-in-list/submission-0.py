class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create hashmap for storing the frequency of occuring of each value
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num , 0)

        # 2- sort the hashmap according to the frequency in ascending order
        arr = []
        for num , freq in count.items():
            arr.append([freq , num])
        
        arr.sort()
        
        result = []
        # 3- loop over the lists of lists for up to k times
        while len(result) < k:
            result.append(arr.pop()[1])

        return result





        