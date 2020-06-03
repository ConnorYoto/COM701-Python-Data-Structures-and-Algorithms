class Node:
    
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def setHead(self, head):
        self.head = head

    def setTail(self, node):
        self.tail = node

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    # Add method -- Complexity is O(1) because we insert records at the beginning of the list
    def add(self, head):
        # create a temporary node
        tempNode = Node(head)
        tempNode.setTail(self.head)
        self.head = tempNode
        del tempNode
        
    # Remove Method -- Complexity is O(N) because we are removing from the list and adjusting the list
    def remove(self, item):
        start = self.head
        previous = None
        found = False
        
        # search element in LinkedList
        while not found:
            if start.getHead() == item:
                found = True
            else:
                previous = start
                start = start.getTail()

        # if previous == None then the data is found at first position
        if previous is None:
            self.head = start.getTail()
        else:
            previous.setTail(start.getTail())
        return found
    
    # Size Method -- Complexity is O(N) because it is iterating through the list and counting all the elements
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getTail()
        # print(size)
        return count
    
    # Search Method -- Complexity is O(N) because it is iterating through n number of times to find a specific value
    def search(self, head):
        current = self.head
        while current:
            if current.getHead() == head:
                return True
            current = current.getTail()
        return False
    
    # Print Method Linked List
    def print(self):
        current = self.head
        if current is None:
            print("Empty List!!!")
            return False

        while current:
            print(str(current.getHead()), end=" ")
            current = current.tail
            if current:
                print("-->", end=" ")
        print()

# Creating Object
myList = LinkedList()

# Creating Elements
myList.add(77)
myList.add(56)
myList.add(49)
myList.add(62)
myList.add(69)

# Proving Created Elements have been populated in the Linked List
myList.print()

# Removing an Element
myList.remove(77)

# Proving 77 was removed
myList.print()

# Finding Size of List
print(myList.size())

# Searching in the List
print(myList.search(49))


