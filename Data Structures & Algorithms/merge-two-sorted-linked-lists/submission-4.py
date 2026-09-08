# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Algorithm Idea:
            - Core Idea: we don't create an additional Node for each processed Node (aka: create new list)
            - That makes space Complexity -> O(n+m) -> (n,m) are number of elements in list-1 and list-2 respectively
            - Core Idea: Merge the Two lists in place:
                a- this will be achieved by having only one node (new_head or DummyNode):
                    N.B: DummyNode (new_head) is fixed doesn't move to have reference to beginning of the merged list
                b- will need another dummy variable to traverse the merged list -> Temp variable
                c- Note: both list-1 and list-2 are pointers to the beginning of each lists respctively
                d- both list-1 & list-2 will change -> we don't need to keep track of original list-1&list-2 begining
                because we are creting a new lsit

            - Algorithm:
            I- Case-1: Both Contain pointers still (no list finished before the other)
                1- compare both list-1 & list-2 Nodes value + start with smaller value (assuming selected smaller val)
                2- chain to DummyNode (new head) 
                3- update list-1 or list-2 pointer (according wich was smaller value)
                4- update temp varaible to move  to new added node in the merged list

            II- Case-2: one of lists (list_1 or list_2) has finished while the other list contain elements
                1- objective: append the list still containing elements to end of (merged lists)
                2- Done by making the last temp pointer to point to the (remaining of list-1 or list-2)

            II- Algorithm Complexity:
                a- Time Complexity: -> O(n+m) due looping over both lists simulatanously + appending
                b- Space Complexity: O(1) we have created only one node and we are changing pointers only
        '''

        # defining both the new_head pointer (strat of lsit) + temp variable (traversing merged list)
        new_head = temp = ListNode()

        # Case-1: Both Contain pointers still (no list finished before the other)
        while list1 and list2:
            # Ste-1: Comparing the values
            if list1.val < list2.val:
                # we don't want to create a new Node
                temp.next = list1
                # update list_1 pointer
                list1 = list1.next                
            else:
                # we don't want to create a new Node
                temp.next = list2
                # update list_1 pointer
                list2 = list2.next

            # update temp node to be the new merged Node (updating the temp variable will occur in both cases)
            # so I extracted it out of loop
            temp = temp.next 

        # Case-2: one of lists (list_1 or list_2) has finished while the other list contain elements
        temp.next = list1 or list2

        return new_head.next








        