class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
            Initialize the:
                a- left pointer
                b- maximum frequency count for a charcter within a given window (current substring)
                c- Dictionary for counting the frequencies of each charcter
        '''
        left = 0
        longest = 0
        max_frequency = 0
        count = {}

        for right in range(len(s)):
            # Count the frequency of character and if not found put a default of zero
            count[s[right]] = 1 + count.get(s[right] , 0)
            max_frequency = max(max_frequency , count[s[right]])

            '''
                Apply the Condition for replacement:
                    a- Case-1: Condition isn't satisfied for replacement (window_size - max_frequency) > k
                        solution: shrink the window from left while condition isn't satisfied

            ''' 
            while ((right - left) + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            longest = max(longest , ((right - left) + 1))
        return longest


        