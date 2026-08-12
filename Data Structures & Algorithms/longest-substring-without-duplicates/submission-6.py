class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Case: The Not Repeated Constraint:
            1- Given an Input array / string
            2- Required: find the length of longest subarray / substring without repeating elements

        I- required Time Complexity: O(n) , n -> length of string
            - left pointer remains at the beginning
            - right pointer moves + when ecnrountering a new character (not duplicate):
                a- add the new element in the hashset
                b- compute the maximum length so far




        II- Required Space  Complexity: O(m) , m -> number of unique characters in string
            - usage of HashSet: stores the unique characters of as string

        '''


        left , right = 0 , 0
        max_length = 0
        seen = set()

        while  right < len(s):
            while s[right] in seen:
                # Step-1: remove from hashset
                seen.remove(s[left])
                # Step-2: increment left pointer
                left +=1

            seen.add(s[right])
            max_length = max(max_length , (right - left + 1))
            right +=1

        return max_length

