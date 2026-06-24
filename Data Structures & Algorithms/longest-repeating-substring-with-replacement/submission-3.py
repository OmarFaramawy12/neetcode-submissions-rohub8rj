class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        I - Algorithm Analysis
            - Idea using Hashmap to count the frequency of characters within a given substring (window)
            - Q: How to know whther the current substring is valid substring or not (aka: if need a number of replacements less than or equal to k -> then it is valid)
            - if it requires a more number of replacements than requested -> not valid (need to decrease the window size)
            - current window size - max Number of the most frequent character = number of replacements to be done within a given substring =< k 

        II- Algorithm Complexity:
            A- Time Complexity:
                -Sliding Window Technique: O(n)
                -building the Hashmap: O(1)
                -hashMap.values(): will loop over the values of the hashmap returning a view (act like a list) -> O(m) where m is nimber of unique characyers in Hashmap
                Note: can Exist a tweak: we don't want to loop over list to extract maximum value 
                        - can have a separate variable that reflexts whats happening in the HAshmap (but this value doesn't decrease -> all it's make is counting maximum)
            B- Space Complexity:
                - O(m): due Hashmap (m is number of unique characyers in Hahsmap)
                - since we are bounded to only 26 characters we say rough;y O(1)

        '''

        hash_map = {}
        left , right = 0,0
        max_substring = 0

        for right in range(len(s)):
            hash_map[s[right]] = 1 + hash_map.get(s[right] , 0)

            while (right-left+1) - max(hash_map.values()) > k:
                hash_map[s[left]] -=1
                left +=1
            
            max_substring = max(max_substring , right-left+1)
        return max_substring






