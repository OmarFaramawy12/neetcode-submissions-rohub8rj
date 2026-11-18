from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # build the freuency counter
        count = defaultdict(int)
        for num in nums:
            count[num] = 1 + count.get(num , 0)
        
        freq_bucket = [[] for i in range(len(nums) + 1)]


        for key , val in count.items():
            freq_bucket[val].append(key)

        res = []
        for i in range(len(freq_bucket) - 1 , 0, -1):
            for num in freq_bucket[i]:
                res.append(num)

                if len(res) == k:
                    return res





