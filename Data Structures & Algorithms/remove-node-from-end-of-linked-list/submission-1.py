# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # phase-1: Traverse the linked list and append each node to array

        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        
        # Phase-2: get the exact index from the beginning of the lsit
        target_index = len(nodes) - n
        # phase-3 Removing the node by relinking the pointers

        # check if node we want to remove is the head -> make head points to the next of current head
        if target_index == 0:
            return head.next


        # re-linking the pointers by making the 
        previous_node = nodes[target_index - 1]
        previous_node.next = nodes[target_index].next
        
        
        return head

       

        