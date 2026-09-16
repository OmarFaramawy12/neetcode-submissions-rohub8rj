"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        '''
        I-Main IDea: (Two Passes + usage of Hashmap)
            - Make copy of original list where a change in the nested properties (Deeper) 
            won't affect the source
            - Each Pointer in new copied list shouldn't point to original Nodes 
                a- Pointers are references
                b- saying in copied list (3 -> random = 5) that would point to the original 
                list
                c- what we want to achieve is make deepy copy for each node in the memory 
                and link the references for these deep copy Nodes together without (new     
                addresses actually not the original addresess for the orignal Nodes)
        
        II- Algorithm:
            N.B: Hashmap will map the original Node to Deep Node
            a- algorithm will require two passes
            b- first pass loop over the linked list to create a deep copy for each node:
                1- for each node create a deep copy node (new location in memory)
                2- Insert the original Node in hashmap and map it to Deep CLoned Node
            
            c- Second Pass: Loop over the original LinkedList + to set-up pointers:
                - Main Idea:  Link the Deep-Copied Nodes with each other ()
                for each node in the original node:
                    1- access it's correspondence deep Node from hashmap
                    2- access the next and Random Nodes from original list + obtain their 
                    corresponding DeepNodes
                    3- Link the Deep Nodes Together
        III- Time Complexiy:
            - first pass - > O(n)
            - Second PAss -> O(n)
            -Total: O(2*n) -> O(n)

        IV- Space Complexity:
            - O(n) (due hashmap size grows with linkedlist size)

        Q: Why we need the hashmap?
            - when setting the next & random pointer of the Deep Node to next Deep Node
            you will discover that you haven't created the deep node for the next node that 
            this node should points to
            - hashmap is needed to map and strore the address of each original Node and it's 
            created deep copy node 
                

        '''

        # Step-1: First Pass: create the Deep Copy foreach Node
        # None: None -> to handle the attribute error if node is None (none->next)
        oldToCopy = {None : None}

        curr = head
        while curr:
            # created a new deep copy node in mempry
            copy = Node(curr.val)
            # MAp the original Node to Deep Copied Node
            oldToCopy[curr] = copy
            curr = curr.next

        # Step-2: Second PAss over original List + setting up the references
        curr = head
        while curr:
            # 1- obtain the correspnding DeepCopied Node
            copy = oldToCopy[curr]
            # 2- obtain the deep copy correspondence of node which curr links to
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

    # step-3: return the head (beginiing of the deep-copy list)
        return oldToCopy[head]
       

        

        