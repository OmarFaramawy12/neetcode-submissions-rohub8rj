# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        Brute Force Algorithm:
            - Main Idea -> I don't need to traverse the entire linked list to get TwinNode
            - Mathematically -> I need to Traverse Middle of linked List (Guranteed to obtain twinNode of entire 
            linked list)
            - Key Question: How to knnow the Index of the TwinNode (since it's not array)
                a- Brute Force Way -> Traverse the Entire Linked List again to find the targer node
                
                Time Comlexity: No of iterations * Work per iteration -> (n/2) * (n) -> (n^2/2)
                Total Time Compelxity: O(n^2)
            
            Guranteed: 
            l1: [5,4]
            l2: [1,2]
            Intuitive Thinking:

                Step-1: Split the Linkedlist into 2 Halves:
                    a- Obtain the Middle of linked-list (using the Fast and Slow Pointer)

                Step-2: Reverse the order of the Second half of the linked-list
                    - main IDea: Reversing Pointers by maintaining a previous Pointer
                    - Return Previous Pointer -> (begining of the reversed second half list)
                    
                Tracking Output till Now:
                    - First Half of the List with pointer pointing to the first element in it
                    - Second half of the List reversed (pointer pointing to  it)

                Step-3: Traverse both 2 lists simulataneously uisng pointers
                    - compute the sum of each Node Value
                    - Return Max value

            
            [5,4]
                L1
            [1,2]
                L2

        '''

        # step-1: Split the list into 2 Halves (obtain the middle of linked list)
        fast , slow = head , head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # output will be slow pointer pointing at the beginning of the second half of list
        #second_half = slow

        # Step-2: Reverse the order of the second half of list

        prev , curr = None , slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # output Prev Pointer is the beginnng of the reversed secondlist

        # Step-3: Traverse the 2 Sublists simulateously  + obtain the sum

        list1 , list2 = head , prev
        twinSum = 0
        twinSumMax = 0
        while list1 and list2:
            twinSum = list1.val + list2.val
            twinSumMax = max(twinSum , twinSumMax)
            # update Pointer
            list1 = list1.next
            list2 = list2.next

        return twinSumMax























        