# Stack: LIFO or FILO
# Method1: Using arrays to implement a stack

class Stack:
    # Create a stack (initialize it to empty)
    def __init__(self):
        self.items = []
    
    # Add an item to the top of the stack
    def push(self, item: any) -> None:
        self.items.append(item)

    # Remove and return the top item from the stack
    def pop(self) -> any:
        if self.isEmpty():
            return None
        return self.items.pop()

    # Return the top item from the stack
    def peek(self) -> any:
        if self.isEmpty():
            return None
        return self.items[-1]
    
    # Check if the stack is empty
    def isEmpty(self) -> bool:
        return len(self.items) == 0
    
    # Return the number of items in the stack
    def size(self) -> int:
        return len(self.items)

    # Return a string representation of the stack
    def __str__(self) -> str:
        return str(self.items)
    
if __name__ == '__main__':
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    print(stack)
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
    print(stack.isEmpty())