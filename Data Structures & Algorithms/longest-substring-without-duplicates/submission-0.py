class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # imitialize the left and the right pointer
        left = 0
        longest_length = 0
        # Set for contasnt lookups and avoiding duplictes
        sett = set()

        # looping over the Array/String using the right pointer as an index:
        for right in range(len(s)):

            # Remove Characters from the Hashmap if while Substring is unvalid (Contains Duplicate):
            while s[right] in sett:
                sett.remove(s[left])
                left +=1

            #Compute the Length of Current Substring
            length = (right - left) + 1

            # Compute the maximum length of longest substring
            longest_length = max(longest_length, length)
            # Add the current character to hashmap
            sett.add(s[right])

        return longest_length



        