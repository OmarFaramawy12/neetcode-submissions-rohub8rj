# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Algorithm Main id;ea: Simple Additon arithmetic + dummy Node Technique (for dealing with edge cases)
            - Main Idea: => Simple addition arthmetic with a taking care of the carry (from previous summation)
            - Looping with both pointers pointing at head of each 2 lists (take into consderation if one is shorter 
            than other)
                a- obtain the nodes values (if node not None)
                b- sum the 2 values together along with carry
                c- obtain the carry alon using Integer diision -> (carry = carry // 10)
                d- obtain the remainder using Modulo operator (value to be inserted into Node) 
                    val = val % 10
            - Edge cases:
                - sum of last 2 nodes have carry -> 
                    a- node1.next & node.next => None (loop should terminate)
                    b- that means we won't able to retun the carry at the end
                    Solution: => in loop condition ->
                - One list is shorter than other
                    a- solution -> you will loop till end of the longer list
                    b- shorter list (means that node is none) -> appned 0 to it's value

            Time Complexity:
                a- O(max(m,n)) -> accounting for the longer list -> O(m+n)
                b- Space complexity:
                    1- extra space -> O(1)
                    2- Output list => O(max(m,n)) = O(m+n)

        
        '''

      
        dummy = ListNode(next = None)
        # temp variable to loop over dummy list
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            '''
            Step-1
            check if node is Not Null -> Obtain value 
            else: -> put value = 0
            '''

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # Step-2: compute sum
            val = v1 + v2 + carry
            # step-3: obtain the carry alon
            carry = val // 10
            # step-4: obtain remainder
            val = val % 10
            curr.next = ListNode(val = val)

            # step-5: update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None



        return dummy.next
