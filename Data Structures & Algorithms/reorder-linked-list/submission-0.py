# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Phase-1: Traversing the Linked List and Putting nodes into array

        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        # Phase-2: Looping ovver the array using the two poointers technique

        left = 0
        right = len(nodes)-1

        while left < right:
            nodes[left].next = nodes[right] 
            left += 1  
            if left >= right:
                break
            nodes[right].next = nodes[left]
            right -= 1

        nodes[left].next = None

        
'''
Algorithmm complexity:

1- Time complexity: O(n)
2- Space complexity: O(n)

'''



        