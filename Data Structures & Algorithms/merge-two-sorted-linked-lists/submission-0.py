# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Algorithm Main idea:
            - create a new empty Node (current varaible used for traversing) and Dummy (resolves the head of list)
            - Traverse Both Linked lists at same Time
            - Compare the Two head pointers together (
                a- Case-1: list1.val < list2.val -> 
                    - append smallest element to Node
                    - update the list1 pointer to points to next element
                b- Case-2: list2.val <= list1.val:
                    - append smallest element to Node
                    - update the list2 pointer to points to next element
            - Update the Node Pointer to point to next item
            Edge Cases: 
                I- Two Lists are the same length -> ideal (algorithm finishes when both next pointer reaches null)
                II- One list is bigger than Other: 
                    - once the shorter list finishes
                    - fill rest with remaining of longer list (append the rest of elements to Dummy Node List)
                   
                    
        '''
         
        # Dummy is essential -> holds the beginning of the list
        # node is variable that moves around 
        # analogy: head is staryt of list
        # you traverse the list with the curr pointer

        dummy = node = ListNode()
        # Case where both lists contain elements
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        # Case-2: if one lists finished before other (still remeaining element in one of list) -> append remaining
        # elements to the node
        node.next = list1 or list2

        return dummy.next   # recall dummy is None Object -> pointing to head of list (dummy.next is first element)

          
    




