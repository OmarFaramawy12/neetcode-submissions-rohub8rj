# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Main Algorithm Idea:
            I- Trafiotoinal Approach: Allocating anew space for each node
                - Traversing the ORiginal Linked List
                - for each node -> :
                    a- create a new node to hold value of current Node
                    b- Save the address (next pointer) in temp variable (due we are changing it's next node)
                    c- set the next pointer of it to new head
                    d- make the head be the new node
                    e- make the current node pointsto temo variable
                - 
                1- Time Complexity: -> O(n)
                    - Traersing the Linked List ony Once

                2- Space Complexity:-> O(n)
                    - Making a new node for each Traversed linked-list
                    - New List size  = original inked list size (O(n))
                    - Total Soace Compleity: space for original List + Space for new list (reversed list)
                         o(n) + O(n) -> O(2n) -> O(n)

            II- Better Approach: single Pass + constant space O(1)

                1- TIme Complexity: - >O(n)
                2- Space Comlexity: O(1)
                    maintaining only pointers
                
             head = [   1   ,   2   ,   3   ,   4   ,   5   ]
                    head,                       curr

        prev = null  
        temp = curr.next (4)            [3 -> 2 -> 1-> null]
                                        prev
        curr.next = prev
        prev = curr
        curr = temp
        '''


        prev , curr = None , head

        while curr:
            # get the next pointer (next node) of the current node
            tmp = curr.next
            # assign the next pointer of current node to points to previous node
            curr.next = prev
            # make the previous Node the current node
            prev = curr
            # assign the current node to point to the temp node (actual ordering in original linked list)
            curr = tmp
            
        return prev
