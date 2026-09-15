# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Main Algorithm : )
            - Two Pointers (Fast and Slow Pointer)
            - First Iteration: advance fast pointer ahead by k over slow (k = n)
            - Second Iteration:
                - advance both the slow pointer and fast pointer by 1 only until reaching end of list
                    - prev = slow
                    - slow = slow.next
                    - Fast = fast.next
                - In each iteration: maintain a prev pointer:
                    a- once reached end
                    b- remove slow Pointer Node:
                        prev.next = slow.next
                        
            - Main Idea: Fast be ahead of slow pointer by kth node (kth Node is n):
            - Looping over list using the fast and slow pointer:
                a- advanve the slow pointer by 1
                b- advance fast pointer by 
        exist edge case: when dealing with 2 Nodes list or  Node List

        '''
     #head = [   1   ,   2   ,   3   ,   4  ],       n = 2
      #  prev,          prev,    s               f

        dummyNode = ListNode(0 , head)
        slow , fast =  dummyNode  , dummyNode
        prev = dummyNode
        # Step-1: Move the Fast pointer ahead of slow pointer by K Nodes (k = n)
        for _ in range(n):
            fast = fast.next


        # Step-2: Second Iteraiton: Advance both the fast and slow pointer untill reaching the end 
        #list

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # Step-3: Output of step-2: Slow pointer Node is the Node we want to remove -> remove it
        prev.next = slow.next

        return dummyNode.next





