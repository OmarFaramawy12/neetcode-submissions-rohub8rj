class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        seen = set()

        for right in range(len(s)):
            # case-1: Duplicates found: remove from set + shrink window
            while s[right] in seen:
                seen.remove(s[left])
                left +=1

            # Case-2: Unique Characters
            seen.add(s[right])
            length = right - left + 1
            max_length = max(length , max_length)

        return max_length

            