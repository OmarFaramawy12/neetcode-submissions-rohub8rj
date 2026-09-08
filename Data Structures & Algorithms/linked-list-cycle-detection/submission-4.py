# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        Main Algorithm: Fast and Slow Pointers:
            -Begin with LSow and Fast Pointers at the hea of list
            - Conditional Checking :-> Fast Pointer and Fast next Pointer doesn't reach the End
                - increment slow pointer by 1
                - increment fast pointer by  2
                - if Intersection Occurs -> Trturn True


        I- Time Complexity: -> O(n):
            A- Case No Cyles
                - Traversign the Entire Linked List once 
                - Fast Pointer visits the (n/2) nodes at most once
                - Slow Pointer visits the other (n/2) nodes at most once
            B- Case exist Cyles
                - Traversign the Entire Linked List once 
                - Fast Pointer visits the cycle nodes at most Twice
                - Slow Pointer visits the Cycle Nodes at most once

        II- Space Complexity: -> O(1)
            - Maintaining Only Pointers

        '''

        slow, fast = head , head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True


        return False
        