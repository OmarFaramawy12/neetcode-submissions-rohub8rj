'''
Designining A Hashmap using open Addressing Technique
    1- Assuming that (Key, value) pair is String (key especially)
    2- Hashmaps are internally built over an array (Array of objects)
    3- where the object is key value pair (key, value) --> Tuple

    3- Handling Collisions using the OPen Addressing Technique
'''

class Pair:
    # defining the pair class 
    def __init__(self , key, value):
        self.key = key
        self.value = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity # How many Tuples the array can store
        self.size = 0 # How many Tuples exist in the array at the beginning
        self.map = [None] * self.capacity # define the array of objects

    def hash(self, key) -> int:
        if type(key) == str:
            index = 0
            for char in key:
                index += ord(char)
            return index % self.capacity
        else:
            return key % self.capacity

        
    def insert(self, key: int, value: int) -> None:
        '''
        Insertion Mehtod:
        - exist two cases:
            1- Inserting a brand new element in the array (new tuple)
                - that will require increasing the size of the array
                - Resizing the array if load factor >= 0.5
                - inserting using Open Addressing

            2- Modifying existing element in array
                - Doesn't require incresing the size of the array
        '''
        index = self.hash(key)
        while True:
            # case-1: inserting a new brand element
            if self.map[index] == None:
                self.map[index] = Pair(key , value)
                self.size +=1
                # checking for the load factor to do resizing (load factor >= 0.5)
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return

            # case-2: modyfing an existing element
            elif self.map[index].key == key:
                self.map[index].value = value
                return

            index +=1
            # modding the index again is becasue if index due incrementing
            # is out of bounds of the array capacity then we return back
            # to the beginning of the array
            index = index % self.capacity # 

    # return value associated with a given key
    def get(self, key: int) -> int:
        '''
        Retrieval Method:
            1- hash key first + search for the hashed key in the Hashmap
            2- Exist 2 Cases:
                - Case_1: Key already exists in map
                    a- using open addressing technique, if hashed key not found 
                    in the given index then increse the pointer by 1 (go down the map)
                    b- caution: while increasing the index (don't go out of bound)
                    c- Once hit an empty slot --> means that element doesn't exist
                - Case_2: Key doesn't exist
                    a- while looping (by using idea of open addressing)
                    b- if an empty  slot found -> then element isn't found
        '''
        index = self.hash(key)
        # exist a key in the bucket
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].value
            elif self.map[index].key != key:
                index +=1
                index = index % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        '''
        Remove Function:
            - given a specified key -> it must remove the tuple (key,value) from Map
            - Removing a Tuples from The Map -> Reduces the Size of the Array
            - Exist 2 Cases:
                a- Case_1: Key Exists (Matches the given index):
                    - Remove Key by decrementing the size (soft Delete) not derefrencing
                    - return True
                b- Case_2: Key Doesn't exists (key at bucket doesn't match hashed index):
                    - using the open addressing: 
                        a- will increase the index
                        b- make sure index doesn't go out of bounds
        '''
        index = self.hash(key)
        # checking that buckets aren't empty
        while self.map[index] != None:
            #Case-1: Key exists (key mathes the hashed index)
            if self.map[index].key == key:
                # soft delete
                self.map[index] = None
                self.size -=1
                return True
            # Case-2: Key doesn't exist (Key in current bucket doesn't match the hashed index Key)
            index +=1
            index = index % self.capacity
        return False

    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        '''
        rehashing Function: 
            1- Doubling the Capacity of the old array
            2- Computing the hashed key for every existing element in
               old hash-map 
            3- Copying the old elements from old Hash-map to new Hash-Map
            Note: Most optimal way is  making the new capacity prime Numer 
                  (Mathematically Proven)
        '''
        # Phase-1: Doubling the Capacity
        self.capacity = 2 * self.capacity
        newMap = [None] * self.capacity
        oldMap = self.map
        self.map = newMap
        # this because the insert method already increments the size when inserting
        # if not resetting the size --> the insert method will continue upon using the old Hashmap size causing a resizing again
        self.size = 0

        # Phase-2: Mpving all the elements from the old Map to new Map
        for pair in oldMap:
            # checking if pair contains elements (Tuple exist)--> Not Null
            if pair:
                self.insert(pair.key, pair.value)



