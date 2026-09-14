# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #creating dummy node to hold the begininng of list + curr to traverse merged lsit
        dummy = curr = ListNode()

        while list1 and list2:

            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            # update the curr pointer in merged list
            curr = curr.next

        # case-2: one of list got empty
        curr.next = list1 or list2

        return dummy.next