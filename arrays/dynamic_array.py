class dynamicArray:
    # Constructor
    def __init__(self, capacity=16): # Default capacity is 16
        self.capacity = capacity 
        self.size = 0 # Number of elements in the array
        self.array = [None] * capacity # Initialize the array with None values
    
    # Get the size of the array
    def getSize(self):
        return self.size

    # Get the capacity of the array
    def getCapacity(self):
        return self.capacity
    
    # Check if the array is empty
    def isEmpty(self):
        return self.size == 0
    
    # Get the element at a specific index
    def get(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        return self.array[index]
    
    # Update the element at a specific index
    def update(self, index, element):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        self.array[index] = element

    # Insert an element at the end of the array
    def append(self, element):
        if self.size == self.capacity: # If the array is full, resize it
            self.resize(2 * self.capacity)
        self.array[self.size] = element
        self.size += 1
    
    # Insert an element at a specific index
    def insert(self, index, element):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.size, index, -1): # Shift elements to the right
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1
    
    # Remove an element at a specific index
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Index out of bounds")
        for i in range(index, self.size - 1): # Shift elements to the left
            self.array[i] = self.array[i + 1]
        self.size -= 1
        if self.size <= self.capacity // 4: # If the array is one-fourth full, resize it
            self.resize(self.capacity // 2)