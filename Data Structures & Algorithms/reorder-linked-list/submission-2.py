# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Algorithm-2: Reverse and Merge the Array:
    1- Phase-1: Dividing the list into 2 halfes (finding the middle of list using fast and slow pointers)
    2- phase-2: Reverse order of the 2nd half of the list
        a- keep track of the first elemment of in the first half -> first pointers
        b- keep track of the first element in the second half of list -> second pointer
        c- make the last element of the first half (slow elment : middle of list) points to null to denote end of list


    3- Phase-3: Merge the 2 lists after reversing the second half of list
'''
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Phase-1: Divide the list into two halfes: this gives the middle element of list to divide from it

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        '''
         Phase-2: Reverse the secons half of the list: using the first and second pointer
            a-returning from this phase the second pointer points to beginning of list after reversing 
              (aka: end element of the original list)
         '''
        second = slow.next
        # denoting the last element of the first half of list point to null denoting end of list
        slow.next = None
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        '''
        Phase-3: Merging the 2 halfs after reversing
            a- by keeping track of the first pointer and second pointer
            b- having temporary variables
        '''
        first, second = head , prev
        while second:
            tmp1 , tmp2 = first.next , second.next
            first.next = second
            second.next = tmp1
            first , second = tmp1 , tmp2

        



        






        
        