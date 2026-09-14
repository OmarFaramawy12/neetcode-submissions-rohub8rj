# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        '''
        Main Idea of Algorithm: 
            - Step-1: Split Linked-list into two Halves: (finding the middle)
                a- using fast and slow pointer
                b- retruning slow pointer -> alsways ensures the middle of list 
                - (slow represent addresss pointing to first element in second list)
                Time Complexity: O(n)

            - Step-2: Rerverse the second half of linked list (reverse order)
                a- reversing done in place by reversing pointers 
                b- having a previous pointer to store revious node
                c- return prev pointer -> (address of the first element in reversed second-half list)
                Time Complexity: O(n)

            - Step-3: Merge the Two sublist togehter:
                a- using the 2 pointers (pointer pointing to list-1 and list-2)
                b- 
                - Time Complexity: O(n)

            - Step-4: Case two sublists  aren't equal in length -> append remaining of longer list to merged 
            list

            - Time Complexity: 
                a- Splitting phase O(n) + reversing O(n) + merging process O(n)
                b- total Time Comlexity: O(3*n) -> O(n)
            - Space Complexity: 
                - Modifying any list is done in place
                - Maintaning only pointer 
                    a- 2 Pointers (Splitting Phase)
                    b- 3 Pointers (prev , curr , temp) -> for reversing phase
                    c- 3 Pointers (curr , first pointer of list-1 , first_pointer of list-2)
                    Total: O(1) 
                whole algorithm: O(1)

            - Note: 
                a- second Half of list contain the Higher location indices
                b- first half of list contains the lower loaction indices
                c- Head of merged list will begin from the first half of the list followed by merging process
                from second part of list
        '''

        # Step-1: Splitting Two lists into 2 halves (finding median)
        fast , slow = head , head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #now slow is median element (slow)

        # Step-2: Reverse ordering of the second-half list
        prev , curr = None , slow.next
        while curr:
            temp = curr.next            
            curr.next = prev            
            prev = curr
            curr = temp

        slow.next = None


        # Step-:3 Merging the 2 Sublists
        list1 , list2 = head , prev
        while list2:                       
            temp1 , temp2 = list1.next , list2.next                            
            list1.next = list2
            list2.next = temp1
            list1 = temp1                                           
            list2 = temp2                                
            

                



