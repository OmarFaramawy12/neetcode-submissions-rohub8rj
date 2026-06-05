from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        bucket_arr = [[] for i in range(len(nums) + 1)]
        # 1- Loop over array to build the hashmap
        for num in nums:    # O(n)
            freq[num] += 1
        #2- loop over the hashmap + building the bucket array
        for key , value in freq.items():
            bucket_arr[value].append(key)

        #3- Extract the top k frequent elements
        # Traverse the Bucket array from the right
        result = []
        for i in range(len(bucket_arr)-1 , 0 , -1):
            for num in bucket_arr[i]:
                result.append(num)
                if len(result) == k:
                    return result

        
        