'''
Node Class:
    - defining a node contain (key, val) pair
    - next, prev pointers

'''
class Node:
    def __init__(self, key ,val):
        self.key , self.val = key , val
        # maintain next , previous pointers
        self.next  = self.prev = None

'''
LRUCache Class (HashMap):
    - small & fast memory holding the MRU elements in memory
    Constructor:
        1- Maintain a fixed capacity of a given size
        2- Initialize the left and Right pointers keep track of LRU element & MRU element Simultaneously
            - Left pointer -> track LRU
            - right pointer -> track MRU
            - left & right pointer must be connected (all the insertion of nodes will be done in middle between them)
    methods:
        1- get:
            - searches the hashmap for a given key if exists:
                a- return the value
                b- track the given node as MRU
        2- put:
            - insert a new element in the cache:
            - check the size of the cache (if cache size >= capacity):
                a- find the LRU element
                b- evict the LRU element
                c- insert the new element

        Helper function dealing with the Doubly Linked List:

        3- insert 
            - maintain 

        4- remove

'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Define an empty hash map
        self.cache = {}
        # Initialize the Dummy left and right pointer to keep track of LRU and MRU elements & connect both of thrm
        self.left , self.right = Node(0,0) , Node(0,0)
        self.left.next , self.right.prev = self.right , self.left
        
    def remove(self , node: Node):
        prevNode , nextNode = node.prev , node.next
        prevNode.next , nextNode.prev = nextNode , prevNode


    def insert(self , node: Node):
        # insertion happens at the End due MRU
        prevNode , nextNode = self.right.prev, self.right
        prevNode.next = nextNode.prev = node
        node.prev , node.next = prevNode , nextNode


    def get(self, key: int) -> int:
        # check if key exists in cache (hashmap)
        if key in self.cache:
            # Maintain Node in the Double Linked List & move element to MRU
            self.remove(self.cache[key])    # remove the LRU element
            self.insert(self.cache[key])    # insert it again to be appened to MRU
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        # case-1: key is already in Cache -> update the value only & move it to MRU
        if key in self.cache:
            self.remove(self.cache[key]) # remove from Double Linked List
        # create a new node 
        # will works either if element is a new node (haven't existed in cache) or we are updating value of an existing element
        self.cache[key] = Node(key , value)
        # 2- Insert in Doubly linked list
        self.insert(self.cache[key])

        # check if the length of hashmap > capacity: evict LRU from hashmap + delete Node from Linked list
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
