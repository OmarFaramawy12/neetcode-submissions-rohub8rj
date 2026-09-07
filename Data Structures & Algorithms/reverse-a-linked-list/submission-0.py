# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Algorithm Idea: (Traditonal Idea) + using Stack
            - Time Complexity: -> O(n) only Looping over the Linked List
            - Space Compleixty: O(1) -> only Miantaining Pointers
        '''
        prev , curr = None , head

        while curr:
            # store the next node in temp variable
            temp = curr.next
            # make the next pointer of current node points to prev node
            curr.next = prev
            # make previos Node be the Current node
            prev = curr
            # update the Current Node to be the Temporary Node (aka: Next Node)
            curr = temp
        return prev
        