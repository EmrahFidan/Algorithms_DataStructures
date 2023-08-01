import ctypes 
# The ctypes library allows you to use data types in language C and manipulate them directly in memory.

class DynamicArray (object):
    
    # initilaize (constructor)
    def __init__(self):
        self.numberVariable = 0
        self.capacity = 1
        self.Array = self.make_array(self.capacity)  
        
    # number of elements in the array 
    def __len__(self):
        return self.numberVariable
    
    # return special index
    def __getitem__(self,index):
        
        # if there is no index entered
        if not 0 <= index < self.numberVariable:
            return IndexError('K is out of bounds!')
        
        return self.Array[index]
    
    # adds element to array
    def append(self, element):
        
        # if the capacity is full
        if self.numberVariable == self.capacity:
            self.__resize(2*self.capacity)  # capacity doubled
            
        self.Array[self.numberVariable] = element # add element
        self.numberVariable += 1 # increase number of elements
        
    # increased the array capacity
    def __resize(self,new_capacity):
        
        # create new array
        new_array = self.make_array(new_capacity)
        
        # copy the elements from the old array to the new array
        for index in range(self.numberVariable):
            new_array[index] = self.Array[index]
            
        # make the new array the old array
        self.Array = new_array
        self.capacity = new_capacity
        
    def make_array(self,new_capacity):
        return (new_capacity * ctypes.py_object)() # create new array
    
    #?  removes element to array
    def remove(self, element):
        # If the element is not in the array, exit the method without doing anything
        if element not in self.Array:
            return

        # Find the index of the element in the array
        index = 0
        while index < self.numberVariable:
            if self.Array[index] == element:
                break
            index += 1

        # Slide other elements using the index to delete the element
        for i in range(index, self.numberVariable - 1):
            self.Array[i] = self.Array[i + 1]

        # Set last element to None and reduce number of elements
        self.Array[self.numberVariable - 1] = None
        self.numberVariable -= 1

        # Equalize array capacity to the number of elements
        self.capacity = self.numberVariable

    # updates element to array
    def update(self, index, new_element):
        # check for a valid index
        if not 0 <= index < self.numberVariable:
            raise IndexError('Invalid index!')

        # update element
        self.Array[index] = new_element  
    


# Test 
array = DynamicArray()
array.append(1)
array.append(5)
array.append(0)
array.append(8)
array.append("emrah")

print("\n")
print("Original array:", [array[i] for i in range(len(array))])

array.remove(0) 

print("\n")
print("Removed array:", [array[i] for i in range(len(array))])
print("\n")

array.update(3, 7)

print("Updated array:", [array[i] for i in range(len(array))])