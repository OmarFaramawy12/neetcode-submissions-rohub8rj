class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0] * capacity
        self.length = 0         # length indicates how many elements are actually in the Array
        

    def get(self, i: int) -> int:
        # Note: if i passed > length --> Raise an Error
        return self.array[i]
        

    def set(self, i: int, n: int) -> None:
        # Note: if i passed > length --> Raise an Error
        # set method doesn't increase the length of array (not inserting a new element in array)
        # set method overwrites an existing element
        self.array[i] = n


    def pushback(self, n: int) -> None:
        # pushback adds an element to the end of the array (increase the length of the array)
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n     # (Reason of using the length as index): Arrays are zero Indexed
        self.length +=1


    def popback(self) -> int:
        # Removing the element from end
        # Recall: Soft deletion (You aren't actually removing the value) --> length variable is the constraint
        if self.length > 0:
            self.length -=1
        return self.array[self.length]

 

    def resize(self) -> None:
        # Step-1: Allocating and doubling the size of previous array
        self.capacity = 2 * self.capacity
        new_array = [0] * self.capacity

        # Step-2: Copying all elements from old array to New Array
        for i in range(self.length):
            new_array[i] = self.array[i]
        self.array = new_array


    def getSize(self) -> int:
        # return the length of array (number of existing elements in array)
        return self.length
    
    def getCapacity(self) -> int:

        return self.capacity
