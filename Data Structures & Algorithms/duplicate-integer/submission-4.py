class Solution:
    '''
    Hashmap Solution:

    '''
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()        # doesn't store the value (only store the keys)
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
            
        