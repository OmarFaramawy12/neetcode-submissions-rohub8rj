class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Case -> the Number of Constraint:
            Given: array / string  + constraint (one distinct character "aka: substring contain the same character")
            Required: longest subarray / substring that contain only one distinct character 

         I- required Time Complexity: O(n) , n -> length of string
            - Valid window: window that I can make K replacement + obtain the longest substring with one distinct charcacte
            - not valid window: after performing the at most k replacement -> won't obtain the largest substring with on
            distinct chracter





        II- Required Space  Complexity: O(m) , m -> number of unique characters in string
            - usage of HashSet: stores the unique characters of as string

                                                             map = {A:4 , B:2}

             s = " A  A   A   B   A   B   B  ",             k = 1 (one replacement)     max_length = 1
               l  r   r   r   r   r                                  
               # A's  , k < = min(#A's , #B's)  -> condition of validity (number of replaements  <= k )
               to know no of replacements : in given window -> will see the least occcuring character -> that will be replaced          No of replacements :(window length - most occuring frequency character)

        '''
                                                       
        
        left , right = 0 ,0
        max_length = 0
        #max_frequent_character = 0
        count = {} 
        for right in range(len(s)):
            # frequency counting
            count[s[right]] = 1 + count.get(s[right] , 0)
            #max_frequent_character = max(max_frequent_character , count(s[right]))

            # condition for not valid window
            while (right - left + 1) - max(count.values()) > k :  
                count[s[left]] -=1
                left +=1        

            max_length = max(max_length , right - left + 1)
        return max_length

