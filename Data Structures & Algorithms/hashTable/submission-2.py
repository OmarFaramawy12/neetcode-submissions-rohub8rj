class Pair:
    def __init__(self, key,value):
        self.key , self.val = key,value

class HashTable:
    
    def __init__(self, capacity: int):
        # Hashtable is built on dynamic array
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity
        
    def hash(self, key) -> int:
        # Checking type of key
        if type(key) == str:
            index = 0
            for char in key:
                index += ord(char)
            return index % self.capacity 
        else:
            return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        # insert element into the array
        index = self.hash(key)
        while True:
            # Case-1: The mapped index is an empty location -> insert directly & Increase the length of Array + check load factor
            if self.map[index] == None:
                self.map[index] = Pair(key , value)
                self.size +=1
                # check the load factror
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            # Case-2: Modifying an Existing element
            elif self.map[index].key == key:
                self.map[index].val = value
                return
            # Case-3: Mapped index is occupied --> use open addressing to insert new element
            index +=1
            index = index % self.capacity
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        # using open addressing (Checking while index is occupied --> aka: contain a key, value pair)
        while self.map[index] != None:
            # Case key matches the desired key
            if self.map[index].key == key:
                return self.map[index].val
            # Case: not matching the desired key:
            elif self.map[index].key != key:
                index +=1
                index = index % self.capacity
        return -1


    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None # Soft Delete
                self.size -= 1
                return True
            # Case-2: the key isn't stored in the desired location (using Open Addressing)
            index +=1
            index = index % self.capacity
    
        return False



    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        # Step-1: Creating a new Map with Doubled capacity
        self.capacity = 2 * self.capacity
        newMap = [None] * self.capacity
        # step-2: Moving old elements from old Map to new Map (with new locations) -> Rehashing
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            # checking if pair not empty
            if pair:
                self.insert(pair.key , pair.val)








