# Initialize a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create a linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Print the list
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

    # Insert a new node at the beginning
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Insert a new node at a specific position
    def insertAtIndex(self, data, index):
        if index < 0 or index > self.getLength():
            print("Invalid index")
            return
        if index == 0:
            self.insertAtBegin(data)
            return
        new_node = Node(data)
        current_node = self.head
        position = 0
        while position < index - 1:
            current_node = current_node.next
            position += 1
        new_node.next = current_node.next
        current_node.next = new_node

    # Delete a node from the beginning
    def deleteFromBegin(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next

    # Delete a node from the end
    def deleteFromEnd(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    # Delete a node from a specific position
    def deleteFromIndex(self, index):
        if index < 0 or index >= self.getLength():
            print("Invalid index")
            return
        if index == 0:
            self.deleteFromBegin()
            return
        current_node = self.head
        position = 0
        while position < index - 1:
            current_node = current_node.next
            position += 1
        current_node.next = current_node.next.next

    # Delete a node with a given value
    def deleteNode(self, value):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next and current_node.next.data != value:
            current_node = current_node.next
        if current_node.next is None:
            print(f"Value '{value}' not found")
            return
        current_node.next = current_node.next.next

    # Search for a specific value
    def search(self, value):
        if self.head is None:
            return "Linked list is empty"
        current_node = self.head
        position = 0
        while current_node:
            if current_node.data == value:
                return position
            current_node = current_node.next
            position += 1
        return "Not Found"

    # Get the length of the linked list
    def getLength(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length

if __name__ == '__main__':
    # Create a new Linked List instance
    llist = LinkedList()

    # Insert each letter at the beginning
    llist.insertAtBegin('e')
    llist.insertAtBegin('d')
    llist.insertAtBegin('c')
    llist.insertAtBegin('b')
    llist.insertAtBegin('a')

    # Insert a letter at the end
    llist.insertAtEnd('f')

    # Insert a letter at a specific position
    llist.insertAtIndex('g', 6)

    # Print the list before deletion
    print("List before deletion:")
    llist.printList()

    # Delete nodes from the beginning, end, and specific position
    llist.deleteFromBegin()
    llist.deleteFromEnd()
    llist.deleteFromIndex(4)
    llist.deleteNode('b')

    # Print the list after deletion
    print("List after deletion:")
    llist.printList()

    # Search for 'c' and 'a' in the list
    print(f"Position of 'c': {llist.search('c')}")  # Expected to find
    print(f"Position of 'a': {llist.search('a')}")  # Expected not to find

    # Print the length of the linked list
    print(f"Size of linked list: {llist.getLength()}")