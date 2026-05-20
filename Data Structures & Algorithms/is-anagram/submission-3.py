class Solution:
    '''
    Sorting Solution:
        - Sorted(s): O(nlog(n)): n is length of  string s
        - Sorted(t): O(mlog(m)): m is length of string t
        - sorted(s) == sorted(t): O(n) (if not same length --> O(1): will not iterate over them)
    
    Algorithm Complexity:
        1- Time Complexity: O(nlogn + mlogm + n) for very large n --> O(nlogn + mlogm)
        2- Space Complexity: O(n+m)
            - creating list conatining sorted elements of s: O(n)
            -creating list conatining sorted elements of t: O(m)
        
        Technically Speaking:
        since sorted(s) & sorted(t) contains the same length due the above checking (m=n)
        Time Complexity: O(2nlogn + n): >>>n --> O(nlogn)
        Space Complexity: O(n+n) -> O(2n) -> O(n)

    '''
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        return sorted(s) == sorted(t)