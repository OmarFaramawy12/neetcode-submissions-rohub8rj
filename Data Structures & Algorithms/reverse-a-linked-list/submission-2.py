# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Main Algorithm:
            - Traverse over each node:
            - hold an auxilary variable to hold the next Node for the Current Node (as we will change pointers)
            - hold previous pointer to hold previous Node:
                a- at start the previous node will be initialized, to NULL
            1- update the current node next pointer to point to Null (indication will be the last node) -> prev pointer
            2- update prev node to be current node (before moving on)
            3- update curr node to point to next node in original list (Temp Node: Auxilary variable)
            4- make temp Node points to new Current Next Node
            Note: will return the Previous Pointer -> it will be pointing to the last current Node (in original-list)
            (first Node in reversed list)

        II- Time Complexity:
            - O(n): only maintaining pointers
        III- Space Complexity:
            - O(1): no auxilary space


            Visual Explanation:
             head = [ 0 , 1 , 2 , 3 ]           cur = head , temp = cur.next , prev = Null
                           pre curr  te
            reversed_list = [ 3-> 2-> 1-> 0-> null] 
        '''
         
        
        # previous pointer pointing to Null , current pointer ppinting to beginning of list
        prev , curr = None, head

        while curr:
            # auxilary variable for holding the next node (due changing pointers)
            temp = curr.next
            # step-1: Set the next pointer of the Current node to point to previous node 
            curr.next = prev
            # Step-2: update Prev pointer
            prev = curr
            # Step-3: Update the Current Node
            curr = temp


        return prev



