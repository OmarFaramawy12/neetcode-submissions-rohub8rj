class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Idea: Using Hash set 
        Hash Set: 1- will take from memory, and in worst case scenario it will be as big as the input array (n)
                  2- Space Complexity: O(n)
                  3- Hash set operations of looking and inserting and deleting is of constant time: O(1)

        A- Solution Complexity:
            Time Complexity: O(n), where hash set insertion is contant time for every element --> O(1)
                             O(1*n) = O(n)

            Space Complexity: O(n) --> In worst case scenario


    
        '''
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False