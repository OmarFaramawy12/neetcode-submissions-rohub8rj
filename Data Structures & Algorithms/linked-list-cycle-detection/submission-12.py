# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        - Main-Idea: Detect Duplicate Nodes (exist several ways)
        1- using Hasmap(Extra Space) -> O(n) holding the n list nodes of the linkedlist:
            - Looping over each node in list and create hashmap out of list 
            - Time Complexity: O(n)
            - Space Complexity: O(n) due Hashmap

        2- Main algorithm: using two pointers 
            - IDea: one moves twice as the other so intersection between the Two pointers guranteed
            - Once Inteersection occurs -> Detected Cycle
            - Fast Pointer and Slow Pointer starts ar the same position
            - Looping over linked list (exit  condition): -> fast pointer reched end Node or fast.next:
                1- increment slow pointer by 1
                2- once intersection occurs -> cycle detected
            -Time Complexity: -> O(n) looping over the linkedlist only once:
                a- Fast pointer visits n/2 nodes
                b- Slow pointer visits other n/2 Nodes
                c- total: O(n/2) + O(n/2) -> O(n) 
            - SPace complexity: O(1) -> amintaining only two pointers (fast and Slow) 
        
        '''

        fast , slow = head , head

        while fast and fast.next:
            # moving the fast pointer ahead by Two
            fast = fast.next.next               # O(1) per iteration
            # moving  the Slow pointer by only one
            slow = slow.next                    # O(1) per iteration

            if slow == fast:                    #checking: O(1) per iteration -> runs O(n) total
                 return True                    # O(1) -> run only once

        return False
