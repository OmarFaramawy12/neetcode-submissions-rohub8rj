from collections import defaultdict

class Solution:
    '''
    Bucket Sort:
        - Having an Additional Array that reflects the Buckets
        - Index of the Bucket array: reflects the number of occurrences of elemenst
        - Number of occurences of elemnts is bounded to the size of array
        -value of the Bucket Array: represents the elements itself in the original array
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary to count the number of occurences of elements in the num array
        freq = defaultdict(int)
        # created the Bucket array + initializing each slot with an empty list
        # len(nums) + 1 --> the size of the array and the (+1) is because the arrays are zero-indexed
        bucket_arr = [[] for _ in range(len(nums) + 1)]
        # Phase-1: Looping over the original array (nums) and create the dictionary
        for num in nums:
            freq[num] +=1

        # phase-2: loopin over the Hashmap (key,value) pair and add them to bucket arr
        for key, value in freq.items():
            bucket_arr[value].append(key)

        #phase-3: Traversing Bucket array from end + extracting the top k Elements
        result = []
        for i in range(len(bucket_arr) - 1,0,-1):
            for num in bucket_arr[i]:
                result.append(num)
                if len(result) == k:
                    return result


                



        