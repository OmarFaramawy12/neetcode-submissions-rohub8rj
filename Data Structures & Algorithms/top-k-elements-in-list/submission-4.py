class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #build hashmap:
        count = {}
        freq_bucket = [[] for i in range(len(nums) + 1)]

        #Step-1: construct Hashmap
        for num in nums:
            count[num] = 1 + count.get(num , 0)


        # Step-2: construct bucket_array
        for key , val in count.items():
            freq_bucket[val].append(key)

        # Step-3: Loop from the end of bucket_array and 
        # extract the top k elements

        res = []

        for occur in range(len(freq_bucket) - 1 , 0 , -1):
            for key in freq_bucket[occur]:
                res.append(key)
                if len(res) == k:
                    return res
