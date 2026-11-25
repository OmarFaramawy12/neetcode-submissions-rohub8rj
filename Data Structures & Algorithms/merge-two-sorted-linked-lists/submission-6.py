# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)        
        curr = dummy
        # Step-1: Break the Tie (see which list you will begin with) -> deciding who is th
        # Dummy Node -> breaks this structure (eliminates the need to checking for fist nodes)
        # Step-: Traversing both list
        # case1: both Two lists have equal number of nodes (Traversing th ewual number of nodes)
        while list1 != None and list2 != None:

            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
            else:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
            

        # case-2: One f the list is bigger than other: appending case
        # checking either of them has a values (while the other is empty)
        rest = list1 or list2
        curr.next = rest

        return dummy.next
                
        