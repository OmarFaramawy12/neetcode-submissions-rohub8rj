# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Brute Force Algorithm:
            - Step-1: traverse the Linked List to count the number of nodes (find the length of list)
            - Determine whther it's even or odd
            - Case-1: Even Length: -> middle is index (n/2)
            - Case-1: Odd length: -> middle is index (n//2) + 1
            - Time Complexity:
                a- O(n) First Loop to determine length
                b- O(n/2) second loop to get middle
                c- Total -> O(n+ n/2) --> O(3n / 2)
        MAin Algorithm: Fast and Slow Pointers (Two Pointers Technique)

            - fast and slow pointer starts at the head
            - Assuming that Fast pointer moves Twice the Speed of SLow Pointer
            -Main Idea-> 
                1- Once the Fast Pointer reaches the End of Linked List -> Slow pointer will be at the 
                middle
                2- This algorithm works better in two cases (even and Odd length linked lIst) 
            -Time Complexity:
                1- O(n) -> Traversing only Once
            - Space Complexity: O(1) -> Maintaining only fast and slow pointers

        '''
        slow , fast = head , head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow

                